
from django.views import View
from django.shortcuts import render, redirect
from sistema.models import Pago, Reserva


class PagosController(View):

    def registrarPago(self, request):

        if request.method == 'POST':
            monto = request.POST.get('monto')
            fecha_pago = request.POST.get('fecha_pago')
            metodo_pago = request.POST.get('metodo_pago')
            reserva_id = request.POST.get('reserva')

            reserva = Reserva.objects.get(id=reserva_id)

            pago = Pago(
                monto=monto,
                fecha_pago=fecha_pago,
                metodo_pago=metodo_pago,
                reserva=reserva
            )

            pago.save()

            return redirect('/pagos/')

        pagos = Pago.objects.all()
        reservas = Reserva.objects.all()

        return render(request, 'pagos.html', {
            'pagos': pagos,
            'reservas': reservas
        })

    def get(self, request):
        return self.registrarPago(request)

    def post(self, request):
        return self.registrarPago(request)
