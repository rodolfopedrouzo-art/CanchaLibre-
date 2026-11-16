
from django.contrib import admin
from django.urls import path

from sistema.controllers.usuarios_controller import UsuariosController
from sistema.controllers.actividades_controller import ActividadesController
from sistema.controllers.canchas_controller import CanchasController
from sistema.controllers.reservas_controller import ReservasController
from sistema.controllers.pagos_controller import PagosController
from sistema.controllers.cancelaciones_controller import CancelacionesController


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', UsuariosController.as_view(), name='inicio'),
    path('actividades/', ActividadesController.as_view(), name='actividades'),
    path('canchas/', CanchasController.as_view(), name='canchas'),
    path('reservas/', ReservasController.as_view(), name='reservas'),
    path('pagos/', PagosController.as_view(), name='pagos'),
    path('cancelaciones/', CancelacionesController.as_view(), name='cancelaciones'),
]



