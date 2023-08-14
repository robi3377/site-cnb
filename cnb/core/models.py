from typing import Any
from django.db import models
from django.utils.translation import gettext_lazy as _

class ExcelFile(models.Model):
    file = models.FileField(upload_to="excel")

# //////////////////////////          PROFESORI          /////////////////////////////////// #

class Profesori(models.Model):
    class Catedre(models.TextChoices):
        MATE = "Matematica", _('MATEMATICA')
        ROMANA_LATINA = "Lb_Romana", _('LIMBA SI LITERATURA ROMANA SI LIMBA LATINA')
        CHIMIE = "Chimie", _('CHIMIE')
        FIZICA = "Fizica", _('FIZICA')
        ENGLEZA = "Limba_Engleza", _('LIMBA ENGLEZA')
        GERMANA = "Limba_Germana", _('LIMBA GERMANA')
        FRANCEZA = "Limba_Franceza", _('LIMBA FRANCEZA')
        GEOGRAFIE = "Geografie", _('GEOGRAFIE')
        INFORMATICA = "Informatica", _('INFORMATICA SI TEHNOLOGIA INFORMATIEI')
        BIOLOGIE = 'Biologie', _('BIOLOGIE')
        ISTORIE = 'Istorie', _('ISTORIE')
        ED_FIZICA = 'Ed_Fizica', _('EDUCATIE FIZICA')
        SOCIO_UMANE = 'Socio_Umane', _('DISCIPLINE SOCIO-UMANE')
        RELIGIE = 'Religie', _('RELIGIE')
        ED_PLASTICA_MUZICALA_TEHNOLOGICA = 'ED_P_M_T', _('EDUCATIE PLASTICA, MUZICALA SI TEHNOLOGICA')

    class Titulaturi(models.TextChoices):
        GRD1 = 'grad 1', _('grad 1')
        GRD2 = 'grad 2', _('grad 2')
        GRD3 = 'grad 3', _('grad 3')
        DEBUTANT = 'Debutant', _('Debutant')
        DEFINITIV = "Definitiv", _('Definitiv')

    prenume = models.CharField(max_length=100, null=True)
    nume = models.CharField(max_length=100, null=True)
    nume_complet = models.CharField(max_length=100, null=True)

    catedra = models.CharField(
        max_length=50,
        choices=Catedre.choices,
        default=None,
        blank=True
    )
    titulatura = models.CharField(
        max_length=20,
        choices=Titulaturi.choices,
        default=Titulaturi.GRD1,
    )
    doctor = models.BooleanField(default=False)
    sef_catedra = models.BooleanField(default=False)

    def __str__(self):
        return self.nume_complet


# //////////////////////////          PROIECTE           /////////////////////////////////// #


class Proiecte(models.Model):
    class Tip(models.TextChoices):
        PAGINI = 'Pagini', _('Pagini')
        PRO_SC = 'Proiect școlar', _('Proiect școlar')
        PRO_EXTSC = 'Activități extrașcolare', _('Activități extrașcolare')
        PRO_CE = 'Proiect consiliul elevilor', _('Proiect consiliul elevilor')


    emblema = models.ImageField(null=True, blank=True)
    titlu = models.CharField(max_length=255)
    tip = models.CharField(
        max_length=30,
        choices=Tip.choices,
        default=Tip.PRO_SC
    )

    def __str__(self):
        return self.titlu
    
class Poze(models.Model):

    poza = models.ImageField(upload_to='poze_proiecte/')
    model = models.ForeignKey(Proiecte, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.model)+str(self.id)
    
class Documente(models.Model):

    document = models.FileField(upload_to='documente_proiecte/')
    model = models.ForeignKey(Proiecte, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.model)+str(self.id)

class Componente(models.Model):
    subtitlu = models.CharField(max_length=255)
    paragraf = models.TextField(max_length=2000)
    model = models.ForeignKey(Proiecte, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.model)+str(self.id)
    
# //////////////////////////          ANUNTURI          /////////////////////////////////// #

import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.date import DateTrigger
from django.db.models.signals import post_save
from django.dispatch import receiver

scheduler = BackgroundScheduler()

def stergere(id):
        model = Anunturi.objects.get(id=id)
        model.delete()

class Anunturi(models.Model):
    class Tip(models.TextChoices):
        ANUNTURI = 'Anunturi', _('Anunturi')
        CONCURSI_ANGAJARE = 'Concursuri angajare', _('Concursuri angajare')

    titlu = models.CharField(max_length=255)
    tip = models.CharField(
        max_length=255, 
        choices=Tip.choices,
        blank=True,
        )
    text = models.TextField(max_length=2000)
    data_stergere = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.titlu
    
@receiver(post_save, sender=Anunturi)
def programare_stergere(sender, instance, created, **kwargs):
    if instance.data_stergere:
        trigger = DateTrigger(run_date=instance.data_stergere+datetime.timedelta(hours=3))
        scheduler.add_job(stergere, args=[instance.id], trigger=trigger)
        if not scheduler.running:
            scheduler.start()
        

# //////////////////////////         OLIMPICI          /////////////////////////////////// #

class Olimpici(models.Model):
    nume = models.CharField(max_length=255)
    anul = models.CharField(max_length=255)
    premiul = models.CharField(max_length=255)
    concursul = models.CharField(max_length=255)
    poza =  models.ImageField(upload_to='poze_olimpici/', blank=True)

    def __str__(self):
        return self.nume

# //////////////////////////         ORGANIZAREA CLASELOR          /////////////////////////////////// #

class Organizare_Clase(models.Model):
    class Clase(models.TextChoices):
        PREG = 'Preg.', _('Preg.')
        I = 'I', _('I')
        II = 'II', _('II')
        III = 'III', _('III')
        IV = 'IV', _('IV')
        V = 'V', _('V')
        VI = 'VI', _('VI')
        VII = 'VII', _('VII')
        VIII = 'VIII', _('VIII')
        IX = 'IX', _('IX')
        X = 'X', _('X')
        XI = 'XI', _('XI')
        XII = 'XII', _('XII')

    diriginte = models.CharField(max_length=255)
    clasa = models.CharField(
        max_length=255,
        choices=Clase.choices)
    litera = models.CharField(max_length=15)
    sala = models.CharField(max_length=255)

    def __str__(self):
        return self.clasa + ' ' + self.litera
    
# //////////////////////////         CONSILIU          /////////////////////////////////// #

class Consiliu(models.Model):
    class Tipuri(models.TextChoices):
        ADMINISTRATIV = 'Consiliu administrativ', _('Consiliu administrativ')
        ELEVILOR = 'Consiliu elevilor', _('Consiliu elevilor')

    nume = models.CharField(max_length=255)
    functie = models.CharField(max_length=255)
    tip = models.CharField(
        max_length=255,
        choices=Tipuri.choices
        )
    
    def __str__(self):
        return self.nume
    
# //////////////////////////         PERSONAL_ADMINISTRATIV          /////////////////////////////////// #

class Personal_administrativ(models.Model):
    nume = models.CharField(max_length=255)
    program = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nume

class Persoane_administrativ(models.Model):
    nume = models.CharField(max_length=255)
    functie = models.CharField(max_length=255)
    model = models.ForeignKey(Personal_administrativ, on_delete=models.PROTECT)

    def __str__(self):
        return self.nume

class Contact_administrativ(models.Model):
    nume = models.CharField(max_length=255)
    telefon = models.CharField(max_length=255)
    model = models.ForeignKey(Personal_administrativ, on_delete=models.PROTECT)

    def __str__(self):
        return self.nume

# //////////////////////////         SEARCH_BAR          /////////////////////////////////// #

class Search_bar(models.Model):
    nume = models.CharField(max_length=255)
    link = models.CharField(max_length=255)

    def __str__(self):
        return self.nume
    
# //////////////////////////         CONSILIUL_ELEVILOR          /////////////////////////////////// #

class Consiliul_elevilor(models.Model):
    nume = models.CharField(max_length=255)
    poza = models.ImageField(upload_to='poze_consiliu/', blank=True)
    functie = models.CharField(max_length=255)
    nr_telefon = models.CharField(max_length=255)
    instagram = models.CharField(max_length=255)

    def __str__(self):
        return self.nume
    
# //////////////////////////         BIBLIOTECA          /////////////////////////////////// #

class Biblioteca(models.Model):
    nume = models.CharField(max_length=500)
    autor = models.CharField(max_length=500)

    def __str__(self):
        return self.nume