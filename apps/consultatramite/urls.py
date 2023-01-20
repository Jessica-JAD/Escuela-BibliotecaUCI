from django.urls import path

from apps.consultatramite.views import CreateConsultaTramite,UpdateConsultaTramite,ListConsultaTramite,DeleteConsultaTramite

urlpatterns = [
    path('lconsultatramite/', ListConsultaTramite.as_view() , name='listarconsultatramite' ),
    path('cconsultatramite/', CreateConsultaTramite.as_view() , name='crearconsultatramite' ),
    path('mconsultatramite/<int:pk>/', UpdateConsultaTramite.as_view() , name='modificarconsultatramite' ),
    path('econsultatramite/<int:pk>/', DeleteConsultaTramite.as_view() , name='eliminarconsultatramite' )
]