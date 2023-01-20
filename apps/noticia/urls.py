from django.urls import path

from apps.noticia.sp_Noticia import CreateNoticia,ListNoticia,DeleteNoticia

urlpatterns = [
    path('lnoticia/', ListNoticia.as_view() , name='listarnoticia' ),
    path('cnoticia/', CreateNoticia.as_view() , name='crearnoticia' ),
    path('enoticia/<int:pk>/', DeleteNoticia.as_view() , name='eliminarnoticia' )
]