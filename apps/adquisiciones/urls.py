from django.urls import path

from apps.adquisiciones.sp_ControladorAdquisiciones import CreateAdquisicion,ListAdquisicion,DeleteAdquisicion

urlpatterns = [
    path('ladquisicion/', ListAdquisicion.as_view() , name='listaradquisicion' ),
    path('cadquisicion/', CreateAdquisicion.as_view() , name='crearadquisicion' ),
    path('eadquisicion/<int:pk>/', DeleteAdquisicion.as_view() , name='eliminaradquisicion' )
]