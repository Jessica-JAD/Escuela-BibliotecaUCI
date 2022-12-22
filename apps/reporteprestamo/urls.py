from django.urls import path

from apps.reporteprestamo.sp_AdministrarReportePrestamoDocumento import CreateReportePrestamo,ListReportePrestamo,DeleteReportePrestamo

urlpatterns = [
    path('lreporteprestamo/', ListReportePrestamo.as_view() , name='listarreporteprestamo' ),
    path('creporteprestamo/', CreateReportePrestamo.as_view() , name='crearreporteprestamo' ),
    path('ereporteprestamo/<int:pk>/', DeleteReportePrestamo.as_view() , name='eliminarreporteprestamo' )
]