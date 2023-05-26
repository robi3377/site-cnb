from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
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
        GRD1 = 'Grad 1', _('Grad 1')
        GRD2 = 'Grad 2', _('Grad 2')
        GRD3 = 'Grad 3', _('Grad 3')
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

class Componente(models.Model):
    subtitlu = models.CharField(max_length=255)
    paragraf = models.TextField(max_length=2000)
    model = models.ForeignKey(Proiecte, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.model)+str(self.id)
    
# //////////////////////////          ANUNTURI          /////////////////////////////////// #

import datetime
class Anunturi(models.Model):
    titlu = models.CharField(max_length=255)
    text = models.TextField(max_length=2000)
    data_delete = models.DateTimeField(blank=True)
    data_created = models.DateTimeField(default=datetime.datetime.today)

    def __str__(self):
        return self.titlu

# //////////////////////////         OLIMPICI          /////////////////////////////////// #

class Olimpici(models.Model):
    nume = models.CharField(max_length=255)
    anul = models.IntegerField()
    premiul = models.CharField(max_length=255)
    concursul = models.CharField(max_length=255)
    poza =  models.ImageField(upload_to='poze_olimpici/', blank=True)

    def __str__(self):
        return self.nume

# //////////////////////////         PROGRAMARI          /////////////////////////////////// #

class Programari(models.Model):
    class Sala(models.TextChoices):
        MULTIMEDIA = 'Multimedia', _('Multimedia')
        FESTIVA = 'Festiva', _('Festiva')


    nume = models.CharField(max_length=255)
    data = models.DateTimeField(default=datetime.datetime.today)
    sala = models.CharField(
        max_length=30,
        choices=Sala.choices
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['data', 'sala'], name='unique_time_location')
        ]

    def __str__(self):
        return self.nume
    
# //////////////////////////         ORGANIZAREA CLASELOR          /////////////////////////////////// #

class Organizare_Clase(models.Model):
    class Clase(models.TextChoices):
        PREG = 'Pregătitoare', _('Pregătitoare')
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
    nr_elevi = models.CharField(max_length=255)

    def __str__(self):
        return self.clasa + ' ' + self.litera