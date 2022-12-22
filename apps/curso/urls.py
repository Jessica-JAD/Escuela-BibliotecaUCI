from django.urls import path

from apps.curso.sp_GestionarCurso import CreateCurso,UpdateCurso,ListCurso,DeleteCurso

urlpatterns = [
    path('lcurso/', ListCurso.as_view() , name='listarcurso' ),
    path('ccurso/', CreateCurso.as_view() , name='crearcurso' ),
    path('mcurso/<int:pk>/', UpdateCurso.as_view() , name='modificarcurso' ),
    path('ecurso/<int:pk>/', DeleteCurso.as_view() , name='eliminarcurso' )
]