from django.urls import path

from apps.plataformauniversitaria.sp_PlataformaUniversitaria import CreatePlatformaUniversitaria,UpdatePlatformaUniversitaria,ListPlatformaUniversitaria,DeletePlatformaUniversitaria

urlpatterns = [
    path('lplataformauniversitaria/', ListPlatformaUniversitaria.as_view() , name='listarplataformauniversitaria' ),
    path('cplataformauniversitaria/', CreatePlatformaUniversitaria.as_view() , name='crearplataformauniversitaria' ),
    path('mplataformauniversitaria/<int:pk>/', UpdatePlatformaUniversitaria.as_view() , name='modificarplataformauniversitaria' ),
    path('eplataformauniversitaria/<int:pk>/', DeletePlatformaUniversitaria.as_view() , name='eliminarplataformauniversitaria' )
]