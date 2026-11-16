
from django.views import View
from django.shortcuts import render, redirect
from sistema.models import Cancha, Actividad


class CanchasController(View):

    def registrarCancha(self, request):

        if request.method == 'POST':
            nombre = request.POST.get('nombre')
            actividad_id = request.POST.get('actividad')

            actividad = Actividad.objects.get(id=actividad_id)

            cancha = Cancha(
                nombre=nombre,
                actividad=actividad
            )

            cancha.save()

            return redirect('/canchas/')

        canchas = Cancha.objects.all()
        actividades = Actividad.objects.all()

        return render(request, 'canchas.html', {
            'canchas': canchas,
            'actividades': actividades
        })

    def get(self, request):
        return self.registrarCancha(request)

    def post(self, request):
        return self.registrarCancha(request)

