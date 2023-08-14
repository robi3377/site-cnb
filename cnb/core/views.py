from django.shortcuts import render
from .models import *
import pandas as pd
from django.contrib.auth.decorators import login_required
from json import dumps
from django.http import JsonResponse
import re
import os
import math

# /////////////////////////// BIBLIOTECA_CARTI //////////////////////////////////

def biblioteca_carti(request, pk):
    if request.method == 'POST':
        cautare = request.POST.get('searchBar')
        carti = Biblioteca.objects.filter(nume__icontains = cautare)
        toate_cartile = list(Biblioteca.objects.all())
        ultima_pagina = math.ceil(len(toate_cartile)/20)

        context = {
            'carti': carti,
            'pagini': ['1', '...', f'{ultima_pagina}'],
        }

        return render(request, 'biblioteca_carti.html', context)
    
    toate_cartile = list(Biblioteca.objects.all())
    carti_pagina = toate_cartile[pk*20-19 : pk*20+1]

    ultima_pagina = math.ceil(len(toate_cartile)/20)

    if pk > ultima_pagina:
        pk = ultima_pagina
    elif pk < 1:
        pk = 1

    
    pagina_curenta = pk
    if pk == 1: 
        pagina_urmatoare = pk+1
        pagina_anterioara = pk
    elif pk == ultima_pagina:
        pagina_urmatoare = pk
        pagina_anterioara = pk-1
    else:
        pagina_urmatoare = pk+1
        pagina_anterioara = pk-1

    pagini = [1, ]
    pagini.append(ultima_pagina)
    pagini.append(pagina_curenta)
    if pagina_curenta > 2:
        pagini.append(pagina_curenta-1)
    if pagina_curenta < ultima_pagina-1:
        pagini.append(pagina_curenta+1)

    pagini = list(set(pagini))
    pagini.sort()
    i = 0
    while(i<len(pagini)-1):
        print(i)
        if pagini[i+1]-pagini[i] > 1:
            pagini.insert(i+1, '...')
            i+=1
        i+=1
    # for i in range(200, 400):
    #     Biblioteca.objects.create(nume=str(i)+'nume', autor=str(i)+'autor')
        
    context = {
        'carti': carti_pagina,
        'pagina_curenta': pagina_curenta,
        'pagina_urmatoare': pagina_urmatoare,
        'pagina_anterioara': pagina_anterioara,
        'pagini': pagini,
    }
    return render(request, 'biblioteca_carti.html', context)

# /////////////////////////// BIBLIOTECA //////////////////////////////////

def biblioteca(request):
    return render(request, 'biblioteca.html')

# /////////////////////////// LOGOPEDIE //////////////////////////////////

def logopedie(request):
    return render(request, 'logopedie.html')

# /////////////////////////// CONSILIUL_ELEVILOR //////////////////////////////////

def consiliul_elevilor(request):
    elevi = list(Consiliul_elevilor.objects.all())
    presedinte = elevi[0]
    elevi.pop(0)

    context = {
        'presedinte': presedinte,
        'elevi': elevi,
    }

    return render(request, 'consiliul_elevilor.html', context)

# /////////////////////////// SEARCH_BAR //////////////////////////////////

def search_bar(request):
    cautari = Search_bar.objects.all().order_by('nume')
    data = {}
    for cautare in cautari:
        data.update({cautare.nume:cautare.link})

    return JsonResponse(data)

# /////////////////////////// PAGINI_DOCUMENTE //////////////////////////////////

def template_doc(request, pk):

    pk = str(pk).replace('_', ' ')
    try:
        model = Proiecte.objects.get(titlu=pk)
    except:
        return render(request, '404.html')
    
    documente = Documente.objects.filter(model=model.id)
    componente = Componente.objects.filter(model=model.id)

    nume=[]
    for doc in documente:
        
        path = str(doc.document)
        filename = os.path.basename(path)
        nume_fara_extensie = re.sub(r'\.[^.]*$', '', filename)

        # Split the filename by hyphens and capitalize the first word
        
        text_curat = nume_fara_extensie.replace('_', ' ')

        nume.append(text_curat)

    doc_cu_nume = zip(documente, nume)

    context = {
        "documente": doc_cu_nume,
        "nume": pk,
        "componente": componente,
    }
    return render(request, 'template_documente.html', context)

# /////////////////////////// PERSONAL_ADMINISTRATIV //////////////////////////////////

def personal_administrativ(request, pk):
    try:
        pk = str(pk).capitalize()
        model = Personal_administrativ.objects.filter(nume=pk).first()
        personal = Persoane_administrativ.objects.filter(model=model.id)
    except:
        return render(request, '404.html')
    
    contact = Contact_administrativ.objects.filter(model=model.id)

    context = {
        'main': model,
        'personal': personal,
        'contact': contact,
    }
    
    return render(request, 'template_administrativ.html', context)

# /////////////////////////// OFERTA_EDUCATIONALA //////////////////////////////////

def oferta_educationala(request):
    return render(request, 'oferta_educationala.html')

# /////////////////////////// CONSILIU //////////////////////////////////

def consiliu(request):

    persoane = Consiliu.objects.filter(tip='Consiliu administrativ')
    context = {}
    nume1 = []
    nume2 = []
    nume3 = []
    nume4 = []
    contor1 = []
    contor2 = []
    contor3 = []
    contor4 = []
    c=0
    cont = 1

    for i in range(len(persoane)):

        if cont == 1:
            nume1.append(persoane[i].nume)
            context.update({persoane[i].nume: persoane[i].functie})
            contor1.append(str(c))
        elif cont == 2:
            nume2.append(persoane[i].nume)
            context.update({persoane[i].nume: persoane[i].functie})
            contor2.append(str(c))
        elif cont == 3:
            nume3.append(persoane[i].nume)
            context.update({persoane[i].nume: persoane[i].functie})
            contor3.append(str(c))
        elif cont == 4:
            nume4.append(persoane[i].nume)
            context.update({persoane[i].nume: persoane[i].functie})
            contor4.append(str(c))

        if cont == 4:
            cont = 1
        else:
            cont += 1

        c+=1

    context_html1 = zip(nume1, contor1)
    context_html2 = zip(nume2, contor2)
    context_html3 = zip(nume3, contor3)
    context_html4 = zip(nume4, contor4)
    json_data = dumps(context)

    return render(request, 'template_consiliu.html', 
                  {'json_data':json_data, 
                   'context_html1':context_html1, 
                   'context_html2':context_html2, 
                   'context_html3':context_html3, 
                   'context_html4':context_html4})

# /////////////////////////// ANUNTURI //////////////////////////////////

def anunturi(request):
    anunturi_raw = Anunturi.objects.filter(tip='Anunturi')
    if len(anunturi_raw) > 0:
        toate_anunturile = list(anunturi_raw)
        anunturi_slide = list(anunturi_raw)
        anunturi_slide.append(toate_anunturile[0])
        
        context = {
            'anunturi_slide': anunturi_slide,
            'anunturi_text': toate_anunturile,
            'tip': 'Anunțuri',
        }
    else:
        context = {
            'tip': 'Anunțuri',
        }

    return render(request, 'anunturi.html', context)

# /////////////////////////// CONCURSURI_ANGAJARE //////////////////////////////////

def concursuri(request):
    concursuri_raw = Anunturi.objects.filter(tip='Concursuri angajare')
    if len(concursuri_raw) > 0:
        toate_concursurile = list(concursuri_raw)
        concursuri_slide = list(concursuri_raw)
        concursuri_slide.append(toate_concursurile[0])

        context = {
            'anunturi_slide':concursuri_slide,
            'anunturi_text':toate_concursurile,
            'tip': 'Concursuri de angajare',
        }
    else:
        context = {
            'tip': 'Concursuri de angajare',
        }

    return render(request, 'anunturi.html', context)
    

# /////////////////////////// OLIMPICI //////////////////////////////////

def olimpici(request):
    toti_olimpicii = Olimpici.objects.all()
    context = {
        'olimpici': toti_olimpicii
    }
    return render(request, 'olimpici.html', context)

# /////////////////////////// INDEX //////////////////////////////////

def index(request):
    home = Proiecte.objects.get(titlu='HOME')
    poze = Poze.objects.filter(model=home.id)
    contor = 1
    cod_poze = []
    for poza in poze:
        if contor == 3 or (contor-3) % 8 == 0:
            x = f'''<div id="bgimage{contor}" onclick="openImagePhone({contor})" onmouseleave="lightup({contor})" onmouseover="darken({contor})" class="bg-no-repeat bg-cover bg-center rounded-3xl duration-500 col-span-2 row-span-2" style="background-image: url({poza.poza.url}); overflow: hidden;">
                <div id="container{contor}" class="w-full h-full bg-slate-300 opacity-50 translate-y-[100%] flex justify-center items-center duration-500">
                    <button onclick="openImage({contor})">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" class="w-24 h-24 duration-500">
                            <path strokeLinecap="round" strokeLinejoin="round" d="M21 21l-5.197-5.197m0 0A7.5 7.5 0 105.196 5.196a7.5 7.5 0 0010.607 10.607z" />
                        </svg>
                    </button> 
                </div>
            </div>'''
            cod_poze.append(x)

        elif contor == 4 or (contor-4) % 8 == 0:
            x = f'''<div id="bgimage{contor}" onclick="openImagePhone({contor})" onmouseleave="lightup({contor})" onmouseover="darken({contor})" class="bg-no-repeat bg-cover bg-center rounded-3xl duration-500 row-span-2 " style="background-image: url({poza.poza.url}); overflow: hidden;">
                        <div id="container{contor}" class="w-full h-full bg-slate-300 opacity-50 translate-y-[100%] flex justify-center items-center duration-500">
                            <button onclick="openImage({contor})">
                                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" class="w-24 h-24 duration-500">
                                <path strokeLinecap="round" strokeLinejoin="round" d="M21 21l-5.197-5.197m0 0A7.5 7.5 0 105.196 5.196a7.5 7.5 0 0010.607 10.607z" />
                                </svg>
                            </button> 
                        </div>
                 </div>'''
            cod_poze.append(x)
            
        else:
            x = f'''<div id="bgimage{contor}" onclick="openImagePhone({contor})" onmouseleave="lightup({contor})" onmouseover="darken({contor})" class="bg-no-repeat bg-cover bg-center rounded-3xl duration-500" style="background-image: url({poza.poza.url}); overflow: hidden;">
                        <div id="container{contor}" class="w-full h-full bg-slate-300 opacity-50 translate-y-[100%] flex justify-center items-center duration-500">
                            <button onclick="openImage({contor})">
                                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" class="w-24 h-24 duration-500">
                                    <path strokeLinecap="round" strokeLinejoin="round" d="M21 21l-5.197-5.197m0 0A7.5 7.5 0 105.196 5.196a7.5 7.5 0 0010.607 10.607z" />
                                </svg>
                            </button> 
                        </div>
                    </div>'''
            cod_poze.append(x)
            
        contor += 1

    context = {
        "poze": cod_poze,
    }

    anunt = list(Anunturi.objects.filter(tip='Anunturi'))

    if len(anunt) > 1:
        anunt.append(anunt[0])
    context.update({"anunturi": anunt,})
    


    return render(request, 'index.html', context)

# /////////////////////////// CATEDRE //////////////////////////////////

def catedre(request):

    catedre = [
    "Matematica",
    "Lb_Romana", 
    "Chimie",
    "Fizica",
    "Limba_Engleza",
    "Limba_Germana",
    "Limba_Franceza",
    "Geografie",
    "Informatica",
    'Biologie',
    'Istorie',
    'Ed_Fizica',
    'Socio_Umane',
    'Religie',
    'ED_P_M_T']

    dic = {}

    for catedra in catedre:
        materie = Profesori.objects.filter(catedra=catedra, sef_catedra=False).order_by('nume')
        sefi_catedre = Profesori.objects.filter(catedra=catedra, sef_catedra=True).order_by('nume')

        sefi = sefi_catedre[:]
        dic.update({f'sefi_{catedra}':sefi})

        materie1 = materie[:int((len(materie)+len(sefi_catedre))/2)-len(sefi_catedre)]
        dic.update({f'{catedra}1':materie1})

        materie2=materie[int((len(materie)+len(sefi_catedre))/2)-len(sefi_catedre):]
        dic.update({f'{catedra}2':materie2})

    return render(request, 'catedre.html', dic)

# /////////////////////////// NOT_FOUND //////////////////////////////////

def not_found(request):
    return render(request, 'decoy.html')

#//////////////////////////////////////////////////

def test(request):
    return render(request, 'test.html')


# ////////////////////////////////////////////////////////////////////

import json
def test1(request):
    data = {
        'test': 'https://www.youtube.com/watch?v=B3vjD41DToU',
        'test2': 'https://stackoverflow.com/questions/24520546/why-is-search-not-defined'
    }
    json_response = json.dumps(data)
    return render(request, 'test.html', {'json_response':json_response})

# /////////////////////////// CONTACT //////////////////////////////////
from django.core.mail import send_mail

def contact(request):
        return render(request, 'contact.html')

# /////////////////////////// INFORMATII //////////////////////////////////

def informatii(request):
    return render(request, 'informatii.html')

# /////////////////////////// ISTORIC //////////////////////////////////

def istoric(request):
    proiect = Proiecte.objects.filter(titlu='ISTORIC').first()
    poze = list(Poze.objects.filter(model=proiect.id))
    poze.append(poze[0])

    context = {
        'poze': poze,
    }
    return render(request, 'istoric.html', context)

# /////////////////////////// ORGANIZAREA CLASELOR //////////////////////////////////

def organizarea_claselor(request):
    clase = [
        'Preg.',
        'I',
        'II',
        'III',
        'IV',
        'V',
        'VI',
        'VII',
        'VIII',
        'IX',
        'X',
        'XI',
        'XII'
    ]

    cod=[]
    contor = 0
    for clasa in clase:
        if contor == 0:
            cod.append('''  <div class="p-2 flex flex-col gap-6">
                            <h1 class="font-noto text-3xl font-bold text-[#123] flex justify-center items-center mb-5">Învățământ primar</h1>
                            ''')
        elif contor == 5:
            cod.append('''  <div class="p-2 flex flex-col gap-6">
                            <h1 class="font-noto text-3xl font-bold text-[#123]  flex justify-center items-center mb-5">Învățământ gimanzial</h1>
                            ''')
        elif contor == 9:
            cod.append('''  <div class="p-2 flex flex-col gap-6">
                            <h1 class="font-noto text-3xl font-bold text-[#123] flex justify-center items-center mb-5">Învățământ liceal</h1>
                            ''')

        if clasa == 'Preg.':
            cod.append('''  <div class="border-2 border-zinc-400 p-4 rounded-3xl">
                            <h2 class="font-noto text-xl font-semibold text-[#762424] border-b-2 border-zinc-400">Clasele pregătitoare</h2>
                            ''')
        elif clasa == 'I':
            cod.append('''  <div class="border-2 border-zinc-400 p-4 rounded-3xl">
                            <h2 class="font-noto text-xl font-semibold text-[#762424] border-b-2 border-zinc-400">Clasele I</h2>
                            ''')
        else:
            cod.append(f'''  <div class="border-2 border-zinc-400 p-4 rounded-3xl">
                            <h2 class="font-noto text-xl font-semibold text-[#762424] border-b-2 border-zinc-400">Clasele a {clasa}-a</h2>
                            ''')
        

        obiecte = Organizare_Clase.objects.filter(clasa=clasa).order_by('litera')

        for obiect in obiecte:
            cod.append('<div class="grid grid-cols-3 w-[100%] md:text-lg text-sm grid-template-column pt-2">')
            if contor < 5:
                cod.append(f'''
                                
                                <p>{obiect.clasa} {obiect.litera}</p>
                                <p>{obiect.diriginte}</p>
                                <p class="justify-self-end">sala {obiect.sala}</p>
                                    
                ''')
            else:
                cod.append(f'''
                                <p>{obiect.clasa} {obiect.litera}</p>
                                <p>{obiect.diriginte}</p>
                                <p class="justify-self-end">sala {obiect.sala}</p>
                ''')
            cod.append('</div>')

        cod.append('</div>')

        if contor == 4 or contor == 8 or contor == 12:
            cod.append('</div>')

        contor+=1
    context = {
        'clase': cod
    }
    return render(request, 'organizarea_claselor.html', context)

# /////////////////////////// ADMINISTRATIV //////////////////////////////////

def administrativ(request):
    return render(request, 'template_administrativ.html')
    

# /////////////////////////// PROIECTE_COSILIUL_ELEVILOR //////////////////////////////////

def proiecte_consiliul_elevilor(request):
    proiecte = Proiecte.objects.filter(tip='Proiect consiliul elevilor')
    context = {
        'proiecte': proiecte
    }

    return render(request, 'proiecte.html', context)

# /////////////////////////// PROIECTE //////////////////////////////////

def proiecte(request):
    proiecte = Proiecte.objects.filter(tip='Proiect școlar')
    context = {
        'proiecte': proiecte
    }

    return render(request, 'proiecte.html', context)

# /////////////////////////// ACTIVITATI_EXTRASCOLARE //////////////////////////////////

def activitati_extrascolare(request):
    proiecte = Proiecte.objects.filter(tip='Activități extrașcolare')
    context = {
        'proiecte': proiecte
    }

    return render(request, 'activitati_extrascolare.html', context)

# /////////////////////////// TEMPLATE_PROIECTE //////////////////////////////////

def template_proiecte(request, pk):
    try:
        proiect = Proiecte.objects.filter(titlu=pk).first()
        componente = Componente.objects.filter(model=proiect.id)

    except:
        return render(request, '404.html')
    
    poze = Poze.objects.filter(model=proiect.id)
    doc = Documente.objects.filter(model=proiect.id)
    contor = 1
    cod_poze = []
    for poza in poze:
        if contor == 3 or (contor-3) % 8 == 0:
            x = f'''<div id="bgimage{contor}" onclick="openImagePhone({contor})" onmouseleave="lightup({contor})" onmouseover="darken({contor})" class="bg-no-repeat bg-cover bg-center rounded-3xl duration-500 col-span-2 row-span-2" style="background-image: url({poza.poza.url}); overflow: hidden;">
                <div id="container{contor}" class="w-full h-full bg-slate-300 opacity-50 translate-y-[100%] flex justify-center items-center duration-500">
                    <button onclick="openImage({contor})">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" class="w-24 h-24 duration-500">
                            <path strokeLinecap="round" strokeLinejoin="round" d="M21 21l-5.197-5.197m0 0A7.5 7.5 0 105.196 5.196a7.5 7.5 0 0010.607 10.607z" />
                        </svg>
                    </button> 
                </div>
            </div>'''
            cod_poze.append(x)

        elif contor == 4 or (contor-4) % 8 == 0:
            x = f'''<div id="bgimage{contor}" onclick="openImagePhone({contor})" onmouseleave="lightup({contor})" onmouseover="darken({contor})" class="bg-no-repeat bg-cover bg-center rounded-3xl duration-500 row-span-2" style="background-image: url({poza.poza.url}); overflow: hidden;">
                        <div id="container{contor}" class="w-full h-full bg-slate-300 opacity-50 translate-y-[100%] flex justify-center items-center duration-500">
                            <button onclick="openImage({contor})">
                                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" class="w-24 h-24 duration-500">
                                <path strokeLinecap="round" strokeLinejoin="round" d="M21 21l-5.197-5.197m0 0A7.5 7.5 0 105.196 5.196a7.5 7.5 0 0010.607 10.607z" />
                                </svg>
                            </button> 
                        </div>
                 </div>'''
            cod_poze.append(x)
            
        else:
            x = f'''<div id="bgimage{contor}" onclick="openImagePhone({contor})" onmouseleave="lightup({contor})" onmouseover="darken({contor})" class="bg-no-repeat bg-cover bg-center rounded-3xl duration-500" style="background-image: url({poza.poza.url}); overflow: hidden;">
                        <div id="container{contor}" class="w-full h-full bg-slate-300 opacity-50 translate-y-[100%] flex justify-center items-center duration-500">
                            <button onclick="openImage({contor})">
                                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" class="w-24 h-24 duration-500">
                                    <path strokeLinecap="round" strokeLinejoin="round" d="M21 21l-5.197-5.197m0 0A7.5 7.5 0 105.196 5.196a7.5 7.5 0 0010.607 10.607z" />
                                </svg>
                            </button> 
                        </div>
                    </div>'''
            cod_poze.append(x)
            
        contor += 1

    if len(doc) < 1:
        check = False
    else:
        check = True

    nume_doc = []
    for d in doc:
        nume = str(d.document).split('/')[-1]
        nume_doc.append(nume)
    
    documente = zip(doc, nume_doc)

    context={
        'proiect': proiect,
        'componente': componente,
        'documente': documente,
        'poze':cod_poze,
        'check': check,
    }
    return render(request, 'template_proiecte.html', context)

# ///////////////////////////////////////////////

# /////////////////////////// INCARCARE_PROIECTE //////////////////////////////////

@login_required(login_url=not_found)
def incarcare_proiecte(request):
    if request.method == 'POST':

        emblema = request.FILES.get('emblema')
        titlu = request.POST.get('titlu')
        subtitlu = request.POST.getlist('subtitlu[]')
        paragraf = request.POST.getlist('paragraf[]')
        tip = request.POST.get('tip')

        proiect = Proiecte.objects.create(titlu=titlu, emblema=emblema, tip=tip)

        for subtitle, paragraph in zip(subtitlu, paragraf):
            if subtitle.strip() == '' and paragraph.strip() == '':
                continue
            else:
                componente = Componente.objects.create(subtitlu=subtitle, paragraf=paragraph, model=proiect)
                componente.save()


        for file in request.FILES.getlist('poze[]'):
            file_type = file.content_type

            if file_type.startswith('image'):
                    poza = Poze.objects.create(poza=file, model=proiect)
                    poza.save()

            else:
                    doc = Documente.objects.create(document=file, model=proiect)
                    doc.save()


        return render(request, 'incarcare_proiect.html')
    else:
        return render(request, 'incarcare_proiect.html')
    
# /////////////////////////// MODIFICARE_PROIECTE //////////////////////////////////

@login_required(login_url=not_found)
def modificare_proiect(request):
    proiecte = Proiecte.objects.all()

    context = {
        'proiecte': proiecte,
    }

    if request.method == 'POST':

        proiect = Proiecte.objects.get(titlu=request.POST.get('tip'))
        
        for file in request.FILES.getlist('poze[]'):
            file_type = file.content_type

            if file_type.startswith('image'):
                    poza = Poze.objects.create(poza=file, model=proiect)
                    poza.save()

            else:
                    doc = Documente.objects.create(document=file, model=proiect)
                    doc.save()


        return render(request, 'modificare_proiect.html', context)
    else:
        return render(request, 'modificare_proiect.html', context)
    
# /////////////////////////// PRELUCRARE_EXCEL //////////////////////////////////

from .models import ExcelFile, Profesori
@login_required(login_url=not_found)
def prelucrare_excel(request):
    if request.method == 'POST':
        response = request.FILES['intake']
        obj = ExcelFile.objects.create(file = response)
        path = response.file
        df = pd.read_excel(path).fillna('').values.tolist()

# ///////////////////// PRIMARA_GIMNAZIU //////////////////////////
        for lista in df:
            litera = str(lista[1]).strip().split('_')[1]
            clasa = str(lista[1]).strip().split('_')[0]
            diriginte = str(lista[2]).title()
            sala = str(lista[3])

            if clasa.lower() == 'preg.':
                obiect = Organizare_Clase.objects.create(
                    diriginte=diriginte,
                    clasa='Preg.',
                    litera=litera, 
                    sala=sala
                    )
            else:
                obiect = Organizare_Clase.objects.create(
                    diriginte=diriginte,
                    clasa=clasa,
                    litera=litera, 
                    sala=sala
                    )
            obiect.save()

# /////////////// LICEU ////////////////////
        # for lista in df:
        #     litera = str(lista[2]).split(' ')[1:]
        #     litera = ' '.join(litera)

        #     clasa = str(lista[2]).split(' ')[0]

        #     diriginte = str(lista[1]).title()
        #     sala = str(lista[4])

        #     obiect = Organizare_Clase.objects.create(
        #         diriginte=diriginte,
        #         clasa=clasa,
        #         litera=litera, 
        #         sala=sala
        #         )
        #     obiect.save()





        # for lis in df[5:-2]:
        #     nume = lis[3]
        #     ini_tata = str(lis[4])
        #     prenume = lis[5]
        #     catedra = str(lis[6])
        #     doc = lis[9]
        #     grad = lis[10]

        #     if catedra == 'FILOSOFIE; LOGICA, ARGUMENTARE SI COMUNICARE':
        #         catedra = 'Socio_Umane'

        #     elif catedra == 'EDUCATIE FIZICA SI SPORT':
        #         catedra = 'Ed_Fizica'

        #     elif catedra == 'MUZICA':
        #         catedra = 'ED_P_M_T'

        #     elif catedra == 'CULTURA CIVICA - STUDII SOCIALE':
        #         catedra = 'Socio_Umane'

        #     elif catedra == 'INVATATOR/INSTITUTOR PENTRU INVATAMANTUL PRIMAR/PROFESOR PENTRU INVATAMANTUL PRIMAR (IN LIMBA ROMANA)':
        #         continue

        #     elif catedra == 'INVATAMANT PRIMAR':
        #         continue

        #     elif catedra == 'INVATATOR/INSTITUTOR PENTRU INVATAMANTUL PRIMAR/PROFESOR PENTRU INVATAMANTUL PRIMAR (IN LIMBA GERMANA)':
        #         continue

        #     elif catedra == 'SOCIOLOGIE':
        #         catedra = 'Socio_Umane'

        #     elif catedra == 'DESEN':
        #         catedra = 'ED_P_M_T'

        #     elif catedra == 'EDUCATIE MUZICALA':
        #         catedra = 'ED_P_M_T'

        #     elif catedra == 'STIINTE SOCIALE':
        #         catedra = 'Socio_Umane'

        #     elif catedra == 'PSIHOLOGIE':
        #         catedra = 'Socio_Umane'

        #     elif catedra == 'LIMBA LATINA':
        #         catedra = 'Lb_Romana'

        #     elif catedra == 'ISTORIE - LIMBA GERMANA':
        #         catedra = 'Istorie'

        #     elif catedra == 'LIMBA SI LITERATURA ROMANA - LITERATURA UNIVERSALA':
        #         catedra = 'Lb_Romana'

        #     elif catedra == 'LIMBA SI LITERATURA ROMANA':
        #         catedra = 'Lb_Romana'

        #     elif catedra == 'RELIGIE ORTODOXA':
        #         catedra = 'Religie'

        #     elif catedra == 'EDUCAȚIE TEHNOLOGICĂ':
        #         catedra = 'ED_P_M_T'

        #     elif catedra == 'EDUCATIE TEHNOLOGICA':
        #         catedra = 'ED_P_M_T'

        #     elif catedra == 'GANDIRE CRITICA':
        #         catedra = 'Socio_Umane'

        #     elif catedra == 'LIMBA ENGLEZA':
        #         catedra = 'Limba_Engleza'

        #     elif catedra == 'LIMBA GERMANA':
        #         catedra = 'Limba_Germana'

        #     elif catedra == 'LIMBA FRANCEZA':
        #         catedra = 'Limba_Franceza'

        #     elif catedra == 'GANDIRE CRITICA':
        #         catedra = 'Socio_Umane'

        #     elif catedra == 'GANDIRE CRITICA':
        #         catedra = 'Socio_Umane'

        #     else:
        #         catedra = catedra.title().strip()
            
        #     if grad == 'GRAD DID I':
        #         grad = 'grad 1'

        #     if grad == 'GRAD DID II':
        #         grad = 'grad 2'

        #     if grad == 'GRAD DID III':
        #         grad = 'grad 3'

        #     if grad == 'GRAD DIDI':
        #         grad = 'grad 1'

        #     if grad == 'GRAD DIDII':
        #         grad = 'grad 2'

        #     if grad == 'GRAD DIDIII':
        #         grad = 'grad 3'

        #     if grad == 'DEBUTANT':
        #         grad = 'Debutant'

        #     if grad == 'DEFINITIV':
        #         grad = 'Definitiv'

        #     if grad == 'DEF':
        #         grad = 'Definitiv'

        #     if grad == 'DOCTORAT':
        #         doc = True
        #         grad = 'grad 1'
        #     else:
        #         if doc == 'DOCTORAT':
        #             doc=True
        #         else:
        #             doc=False

        #     if ini_tata == '':
        #         pass
        #     else:
        #         if ini_tata.strip()[-1] != '.':
        #             ini_tata = ini_tata+'.'


        #         prenume = str(prenume).title()
        #         prenume_f = str(prenume)+' '+str(ini_tata)

        #     nume = str(nume)
            
        #     pr = Profesori.objects.create( 
        #         prenume = prenume_f,
        #         nume = nume,
        #         nume_complet = prenume_f + ' ' + nume,
        #         catedra = catedra, 
        #         titulatura = grad,
        #         doctor = doc,
        #         sef_catedra = False
        #         )
    return render(request, 'prelucrare_excel.html')
