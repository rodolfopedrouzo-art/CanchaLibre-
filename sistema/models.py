
from django.db import models


class Cliente(models.Model):
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    telefono = models.CharField(max_length=45)


class Actividad(models.Model):
    nombre = models.CharField(max_length=45)


class Cancha(models.Model):
    nombre = models.CharField(max_length=45)
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE)


class Reserva(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    cancha = models.ForeignKey(Cancha, on_delete=models.CASCADE)


class Pago(models.Model):
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_pago = models.DateField()
    metodo_pago = models.CharField(max_length=45)
    reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE)


class Cancelacion(models.Model):
    motivo = models.CharField(max_length=45)
    fecha_cancelacion = models.CharField(max_length=45)
    reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE)
