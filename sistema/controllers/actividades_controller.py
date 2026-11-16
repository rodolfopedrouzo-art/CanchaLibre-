
from django.views import View
from django.shortcuts import render, redirect
from sistema.models import Actividad


class ActividadesController(View):

    def registrarActividad(self, request):

        if request.method == 'POST':
            nombre = request.POST.get('nombre')

            actividad = Actividad(
                nombre=nombre
            )

            actividad.save()

            return redirect('/actividades/')

        actividades = Actividad.objects.all()

        return render(request, 'actividades.html', {
            'actividades': actividades
        })

    def get(self, request):
        return self.registrarActividad(request)

    def post(self, request):
        return self.registrarActividad(request)
