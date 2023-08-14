from django.contrib import admin
from .models import Profesori, ExcelFile, Proiecte, Documente, Poze, Componente, Anunturi, Olimpici, Organizare_Clase, Consiliu, Consiliul_elevilor, Persoane_administrativ, Personal_administrativ, Contact_administrativ, Search_bar, Biblioteca

class ProfesoriAdmin(admin.ModelAdmin):
    search_fields = ['nume', 'prenume', 'catedra', 'titulatura', 'doctor']
    list_display = ['nume_complet', 'catedra', 'titulatura', 'doctor']

class ProiecteAdmin(admin.ModelAdmin):
    search_fields = ['titlu', 'tip']
    list_display = ['titlu', 'tip']

class PozeAdmin(admin.ModelAdmin):
    search_fields = ['model__titlu']
    
class ComponenteAdmin(admin.ModelAdmin):
    search_fields = ['model__titlu', 'subtitlu']
    
class DocumenteAdmin(admin.ModelAdmin):
    search_fields = ['model__titlu', 'document']

admin.site.register(Profesori, ProfesoriAdmin)
admin.site.register(ExcelFile)
admin.site.register(Proiecte, ProiecteAdmin)
admin.site.register(Documente, DocumenteAdmin)
admin.site.register(Poze, PozeAdmin)
admin.site.register(Componente, ComponenteAdmin)
admin.site.register(Anunturi)
admin.site.register(Olimpici)
admin.site.register(Organizare_Clase)
admin.site.register(Consiliu)
admin.site.register(Consiliul_elevilor)
admin.site.register(Personal_administrativ)
admin.site.register(Persoane_administrativ)
admin.site.register(Contact_administrativ)
admin.site.register(Search_bar)
admin.site.register(Biblioteca)

