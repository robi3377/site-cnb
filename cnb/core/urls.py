from django.urls import path
from . import views

urlpatterns = [

    path('', views.index),
    path('catedre', views.catedre),
    path('contact', views.contact),
    path('informatii', views.informatii),
    path('informatii/personal_administrativ/<str:pk>', views.personal_administrativ),
    path('informatii/<str:pk>', views.template_doc),
    path('istoric', views.istoric),
    path('organizarea_claselor', views.organizarea_claselor),
    path('activitati_extrascolare', views.activitati_extrascolare),
    path('proiecte', views.proiecte),
    path('consiliul_elevilor_proiecte', views.proiecte_consiliul_elevilor),
    path('incarcare_proiect', views.incarcare_proiecte),
    path('modificare_proiect', views.modificare_proiect),
    path('prelucrare_excel', views.prelucrare_excel),
    path('anunturi', views.anunturi),
    path('logopedie', views.logopedie),
    path('concursuri_de_angajare', views.concursuri),
    path('olimpici', views.olimpici),
    path('biblioteca', views.biblioteca),
    path('biblioteca_carti<int:pk>', views.biblioteca_carti),
    path('secretariat', views.administrativ),
    path('proiecte/<str:pk>', views.template_proiecte),
    path('activitati_extrascolare/<str:pk>', views.template_proiecte),
    path('test', views.search_bar),
    # path('test_js', views.test_js),
    path('consiliul_administrativ', views.consiliu),
    path('consiliul_elevilor', views.consiliul_elevilor),
    path('oferta_educationala', views.oferta_educationala),
    path('404', views.not_found),

]