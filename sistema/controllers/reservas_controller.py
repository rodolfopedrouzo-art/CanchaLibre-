
from django.views import View
from django.shortcuts import render, redirect
from sistema.models import Reserva, Cliente, Cancha, Cancelacion


class ReservasController(View):

    def registrarReserva(self, request):

        if request.method == 'POST':
            fecha = request.POST.get('fecha')
            hora = request.POST.get('hora')
            cliente_id = request.POST.get('cliente')
            cancha_id = request.POST.get('cancha')

            cliente = Cliente.objects.get(id=cliente_id)
            cancha = Cancha.objects.get(id=cancha_id)

            reservas_canceladas = Cancelacion.objects.values(
                'reserva_id'
            )

            reserva_existente = Reserva.objects.filter(
                fecha=fecha,
                hora=hora,
                cancha=cancha
            ).exclude(
                id__in=reservas_canceladas
            ).exists()

            if not reserva_existente:
                reserva = Reserva(
                    fecha=fecha,
                    hora=hora,
                    cliente=cliente,
                    cancha=cancha
                )

                reserva.save()

            return redirect('/reservas/')

        reservas = Reserva.objects.all()
        clientes = Cliente.objects.all()
        canchas = Cancha.objects.all()

        return render(request, 'reservas.html', {
            'reservas': reservas,
            'clientes': clientes,
            'canchas': canchas
        })

    def get(self, request):
        return self.registrarReserva(request)

    def post(self, request):
        return self.registrarReserva(request)

