from django.urls import path

from apps.traducciondocumento.sp_traduccionDocumento import CreateTraduccionDocumento,ListTraduccionDocumento,DeleteTraduccionDocumento

urlpatterns = [
    path('ltraducciondocumento/', ListTraduccionDocumento.as_view() , name='listartraducciondocumento' ),
    path('ctraducciondocumento/', CreateTraduccionDocumento.as_view() , name='creartraducciondocumento' ),
    path('etraducciondocumento/<int:pk>/', DeleteTraduccionDocumento.as_view() , name='eliminartraducciondocumento' )
]