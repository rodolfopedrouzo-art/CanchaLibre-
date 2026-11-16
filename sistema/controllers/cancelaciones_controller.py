
from django.views import View
from django.shortcuts import render, redirect
from sistema.models import Cancelacion, Reserva
from datetime import date


class CancelacionesController(View):

    def registrarCancelacion(self, request):

        if request.method == 'POST':
            motivo = request.POST.get('motivo')
            reserva_id = request.POST.get('reserva')

            reserva = Reserva.objects.get(id=reserva_id)

            cancelacion = Cancelacion(
                motivo=motivo,
                fecha_cancelacion=str(date.today()),
                reserva=reserva
            )

            cancelacion.save()

            return redirect('/cancelaciones/')

        cancelaciones = Cancelacion.objects.all()
        reservas = Reserva.objects.exclude(
            id__in=Cancelacion.objects.values('reserva_id')
        )

        return render(request, 'cancelaciones.html', {
            'cancelaciones': cancelaciones,
            'reservas': reservas
        })

    def get(self, request):
        return self.registrarCancelacion(request)

    def post(self, request):
        return self.registrarCancelacion(request)
