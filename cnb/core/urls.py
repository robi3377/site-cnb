from django.urls import path
from . import views

urlpatterns = [

    path('', views.index),
    path('catedre', views.catedre),
    path('contact', views.contact),
    path('informatii', views.informatii),
    path('istoric', views.istoric),
    path('organizarea_claselor', views.organizarea_claselor),
    path('activitati_extrascolare', views.activitati_extrascolare),
    path('proiecte', views.proiecte),
    path('incarcare_proiect', views.incarcare_proiecte),
    path('template_noutati', views.template_noutati),
    path('template', views.template),
    path('database', views.database),
    path('anunturi', views.anunturi),
    path('olimpici', views.olimpici),
    path('programari', views.programari),
    path('proiecte/<str:pk>', views.template_proiecte),
    path('404', views.not_found),

]