from django.contrib import admin
from .models import Profesori, ExcelFile, Proiecte, Poze, Componente, Anunturi, Olimpici, Programari, Organizare_Clase

class ProfesoriAdmin(admin.ModelAdmin):
    search_fields = ['nume', 'prenume', 'catedra', 'titulatura', 'doctor']
    list_display = ['nume_complet', 'catedra', 'titulatura', 'doctor']


admin.site.register(Profesori, ProfesoriAdmin)
admin.site.register(ExcelFile)
admin.site.register(Proiecte)
admin.site.register(Poze)
admin.site.register(Componente)
admin.site.register(Anunturi)
admin.site.register(Olimpici)
admin.site.register(Programari)
admin.site.register(Organizare_Clase)

