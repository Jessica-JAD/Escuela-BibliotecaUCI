from django.urls import path

from apps.bibliografia.sp_GestionarBibliografiaEspecializada import CreateBibliografia,UpdateBibliografia,ListBibliografia,DeleteBibliografia

urlpatterns = [
    path('lbibliografia/', ListBibliografia.as_view() , name='listarbibliografia' ),
    path('cbibliografia/', CreateBibliografia.as_view() , name='crearbibliografia' ),
    path('mbibliografia/<int:pk>/', UpdateBibliografia.as_view() , name='modificarbibliografia' ),
    path('ebibliografia/<int:pk>/', DeleteBibliografia.as_view() , name='eliminarbibliografia' )
]