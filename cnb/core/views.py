from django.shortcuts import render
from .models import *
import pandas as pd

# /////////////////////////// ANUNTURI //////////////////////////////////

def anunturi(request):
    toate_anunturile = Anunturi.objects.all()
    context = {
        'anunturi':toate_anunturile
    }
    return render(request, 'anunturi.html', context)

# /////////////////////////// OLIMPICI //////////////////////////////////

def olimpici(request):
    toti_olimpicii = Olimpici.objects.all()
    context = {
        'olimpici': toti_olimpicii
    }
    return render(request, 'olimpici.html', context)

# /////////////////////////// PROGRAMARI //////////////////////////////////

import datetime
def programari(request):

    today = datetime.date.today()
    current_weekday = today.weekday()  # Get the weekday (0 for Monday, 6 for Sunday)
    start_of_week = today - datetime.timedelta(days=current_weekday)  # Calculate the start of the week
    zilele_saptamanii = [start_of_week + datetime.timedelta(days=i) for i in range(5)]  # Generate a list of dates for the week

    context = {}
    cod_programari = []
    sali = ['Multimedia', 'Festiva']

    for sala in sali:
        for zi in zilele_saptamanii:
            
            cod_programari.append('<div class="w-[100%] h-[100%] border-2 flex flex-col text-base text-white">')

            for i in range(7):

                programare = Programari.objects.filter(data=f'{zi} {8+i}:00:00', sala=sala).first()

                if programare:
                    cod = f'<div class="w-[100%] h-[15%] border-2 bg-[#762424] flex justify-center items-center rounded-md">{programare}</div>'
                    cod_programari.append(cod)
                    
                else:
                    cod='<div class="w-[100%] h-[15%] border-2"></div>'
                    cod_programari.append(cod)

            cod_programari.append('</div>')

        context.update({f'programari_{sala}':cod_programari})
        cod_programari = []

    return render(request, 'programari.html', context)

# /////////////////////////// INDEX //////////////////////////////////

def index(request):
    home = Proiecte.objects.get(titlu='HOME')
    poze = Poze.objects.filter(model=home.id)
    contor = 1
    cod_poze = []
    for poza in poze:
        if contor == 3 or (contor-3) % 8 == 0:
            x = f'''<div id="bgimage{contor}" onclick="openImagePhone({contor})" onmouseleave="lightup({contor})" onmouseover="darken({contor})" class="bg-no-repeat bg-cover bg-center rounded-3xl duration-500 col-span-2 row-span-2" style="background-image: url(./assets/{poza.poza}); overflow: hidden;">
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
            x = f'''<div id="bgimage{contor}" onclick="openImagePhone({contor})" onmouseleave="lightup({contor})" onmouseover="darken({contor})" class="bg-no-repeat bg-cover bg-center rounded-3xl duration-500 row-span-2" style="background-image: url(./assets/{poza.poza}); overflow: hidden;">
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
            x = f'''<div id="bgimage{contor}" onclick="openImagePhone({contor})" onmouseleave="lightup({contor})" onmouseover="darken({contor})" class="bg-no-repeat bg-cover bg-center rounded-3xl duration-500" style="background-image: url(./assets/{poza.poza}); overflow: hidden;">
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
        'poze': cod_poze,
    }
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
    print(dic)
    return render(request, 'catedre.html', dic)

# ///////////////////////////////////////////////////////////////

from .models import Proiecte
def test(request):
#     proiect = Proiecte.objects.get(titlu='Test1')
#     componente = Componente.objects.filter(model=proiect.id)
#     poze = Poze.objects.filter(model=proiect.id)

    context = {
        # 'proiect': proiect,
        # 'componente': componente,
        # 'poze': poze,
        'comanda': '<p style="color: red;">TEST</p>'
    }
    return render(request, 'test.html', context)
# ///////////////////////////////////////////////////////////////

# /////////////////////////// INCARCARE_PROIECTE //////////////////////////////////

def incarcare_proiecte(request):
    if request.method == 'POST':
    
        emblema = request.FILES.get('emblema')
        titlu = request.POST.get('titlu')
        subtitlu = request.POST.getlist('subtitlu[]')
        paragraf = request.POST.getlist('paragraf[]')
        tip = request.POST.get('tip')
        poze = request.FILES.getlist('poze[]')

        proiect = Proiecte.objects.create(titlu=titlu, emblema=emblema, tip=tip)
        print(subtitlu)
        print(poze)

        for subtitle, paragraph in zip(subtitlu, paragraf):
            if subtitle.strip() == '' and paragraph.strip() == '':
                continue
            else:
                componente = Componente.objects.create(subtitlu=subtitle, paragraf=paragraph, model=proiect)
                componente.save()
        
        for p in poze:
            poza = Poze.objects.create(poza=p, model=proiect)
            poza.save()


        return render(request, 'incarcare_proiect.html')
    else:
        return render(request, 'incarcare_proiect.html')

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
    if request.method == 'POST':

        nume = request.POST.get('nume')
        email = request.POST.get('email')
        subiect = request.POST.get('subiect')
        mesaj = request.POST.get('mesaj')

        subject = f"{subiect} (Primit de la {nume})"
        email_body = f"Nume: {nume}\nEmail: {email}\nMesaj: {mesaj}"
        sender_email = 'robert.uibar@outlook.com'
        receiver_email = 'robert.uibar@gmail.com'
        send_mail(subject, email_body, sender_email, [receiver_email], fail_silently=False,)

        return render(request, 'contact.html')
    else:
        return render(request, 'contact.html')


def informatii(request):
    return render(request, 'informatii.html')

def istoric(request):
    return render(request, 'istoric.html')

# /////////////////////////// ORGANIZAREA CLASELOR //////////////////////////////////

def organizarea_claselor(request):
    clase = [
        'Pregătitoare',
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

        if clasa == 'Pregătitoare':
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
            if contor < 5:
                cod.append(f'''
                                <div class="flex flex-col">
                                    <div class="flex text-base md:text-lg gap-3 pt-2">
                                        <p>{obiect.clasa} {obiect.litera}</p>
                                        <p>învățătoare {obiect.diriginte}</p>
                                        <p>{obiect.nr_elevi}</p>
                                    </div>
                                </div>
                ''')
            else:
                cod.append(f'''
                                <div class="flex flex-col">
                                    <div class="flex text-base md:text-lg gap-3 pt-2">
                                        <p>{obiect.clasa} {obiect.litera}</p>
                                        <p>diriginte {obiect.diriginte}</p>
                                        <p>{obiect.nr_elevi}</p>
                                    </div>
                                </div>
                ''')

        cod.append('</div>')

        if contor == 4 or contor == 8 or contor == 12:
            cod.append('</div>')

        contor+=1
    context = {
        'clase': cod
    }
    return render(request, 'organizarea_claselor.html', context)

# /////////////////////////// PROIECTE //////////////////////////////////

def proiecte(request):
    proiect = Proiecte.objects.filter(tip='Proiect școlar')
    context = {
        'proiecte': proiect
    }
    print(proiect)
    return render(request, 'proiecte.html', context)

# /////////////////////////// ACTIVITATI EXTRASCOLARE //////////////////////////////////

def activitati_extrascolare(request):
    proiect = Proiecte.objects.filter(tip='Activități extrașcolare')
    context = {
        'proiecte': proiect
    }
    print(proiect)
    return render(request, 'activitati_extrascolare.html', context)

# /////////////////////////// TEMPLATE_PROIECTE //////////////////////////////////

def template_proiecte(request, pk):
    proiect = Proiecte.objects.get(titlu=pk)
    componente = Componente.objects.filter(model=proiect.id)
    poze = Poze.objects.filter(model=proiect.id)
    contor = 1
    cod_poze = []
    for poza in poze:
        if contor == 3 or (contor-3) % 8 == 0:
            x = f'''<div id="bgimage{contor}" onclick="openImagePhone({contor})" onmouseleave="lightup({contor})" onmouseover="darken({contor})" class="bg-no-repeat bg-cover bg-center rounded-3xl duration-500 col-span-2 row-span-2" style="background-image: url(./assets/{poza.poza}); overflow: hidden;">
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
            x = f'''<div id="bgimage{contor}" onclick="openImagePhone({contor})" onmouseleave="lightup({contor})" onmouseover="darken({contor})" class="bg-no-repeat bg-cover bg-center rounded-3xl duration-500 row-span-2" style="background-image: url(./assets/{poza.poza}); overflow: hidden;">
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
            x = f'''<div id="bgimage{contor}" onclick="openImagePhone({contor})" onmouseleave="lightup({contor})" onmouseover="darken({contor})" class="bg-no-repeat bg-cover bg-center rounded-3xl duration-500" style="background-image: url(./assets/{poza.poza}); overflow: hidden;">
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

    context={
        'proiect': proiect,
        'componente': componente,
        'poze':cod_poze
    }
    return render(request, 'template_proiecte.html', context)

def template(request):
    return render(request, 'template.html')

def template_noutati(request):
    return render(request, 'template_noutati.html')


from .models import ExcelFile, Profesori

def database(request):
    if request.method == 'POST':
        response = request.FILES['intake']
        obj = ExcelFile.objects.create(file = response)
        path = response.file
        df = pd.read_excel(path).fillna('').values.tolist()
        for lista in df:
            litera = str(lista[1]).strip().split('_')[1]
            clasa = str(lista[1]).strip().split('_')[0]
            diriginte = str(lista[2]).title()
            nr_elevi = lista[3]

            if clasa == 'PREG.':
                obiect = Organizare_Clase.objects.create(
                    diriginte=diriginte,
                    clasa='Pregătitoare',
                    litera=litera, 
                    nr_elevi=nr_elevi
                    )
            else:
                obiect = Organizare_Clase.objects.create(
                    diriginte=diriginte,
                    clasa=clasa,
                    litera=litera, 
                    nr_elevi=nr_elevi
                    )
            obiect.save()

        # for lista in df:
        #     litera = str(lista[2]).split(' ')[1:]
        #     litera = ' '.join(litera)
        #     print(litera)
        #     clasa = str(lista[2]).split(' ')[0]
        #     print(clasa)
        #     diriginte = str(lista[1]).title()
        #     nr_elevi = lista[3]

        #     obiect = Organizare_Clase.objects.create(
        #         diriginte=diriginte,
        #         clasa=clasa,
        #         litera=litera, 
        #         nr_elevi=nr_elevi
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
        #         grad = 'Grad 1'

        #     if grad == 'GRAD DID II':
        #         grad = 'Grad 2'

        #     if grad == 'GRAD DID III':
        #         grad = 'Grad 3'

        #     if grad == 'GRAD DIDI':
        #         grad = 'Grad 1'

        #     if grad == 'GRAD DIDII':
        #         grad = 'Grad 2'

        #     if grad == 'GRAD DIDIII':
        #         grad = 'Grad 3'

        #     if grad == 'DEBUTANT':
        #         grad = 'Debutant'

        #     if grad == 'DEFINITIV':
        #         grad = 'Definitiv'

        #     if grad == 'DEF':
        #         grad = 'Definitiv'

        #     if grad == 'DOCTORAT':
        #         doc = True
        #         grad = 'Grad 1'
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
    return render(request, 'database.html')
