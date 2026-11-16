
from django.views import View
from django.shortcuts import render, redirect
from sistema.models import Cliente


class UsuariosController(View):

    def registrarUsuario(self, request):

        if request.method == 'POST':
            nombre = request.POST.get('nombre')
            apellido = request.POST.get('apellido')
            email = request.POST.get('email')
            telefono = request.POST.get('telefono')

            cliente = Cliente(
                nombre=nombre,
                apellido=apellido,
                email=email,
                telefono=telefono
            )

            cliente.save()

            return redirect('/')

        clientes = Cliente.objects.all()

        return render(request, 'index.html', {'clientes': clientes})

    def get(self, request):
        return self.registrarUsuario(request)

    def post(self, request):
        return self.registrarUsuario(request)

