from django.urls import path

from apps.asistenciaespecializada.sp_asistenciaEspecializada import CreateAsistenciaEspecializada,ListAsistenciaEspecializada,DeleteAsistenciaEspecializada, UpdateAsistenciaEspecializada

urlpatterns = [
    path('lasistenciaespecializada/', ListAsistenciaEspecializada.as_view() , name='listarasistenciaespecializada' ),
    path('casistenciaespecializada/', CreateAsistenciaEspecializada.as_view() , name='crearasistenciaespecializada' ),
    path('masistenciaespecializada/<int:pk>/', UpdateAsistenciaEspecializada.as_view() , name='modificarasistenciaespecializada' ),
    path('easistenciaespecializada/<int:pk>/', DeleteAsistenciaEspecializada.as_view() , name='eliminarasistenciaespecializada' )
]