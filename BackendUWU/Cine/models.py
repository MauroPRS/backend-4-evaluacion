from django.db import models
# Create your models here.
tipoFuncionChoice=[
    ("3D","3D"),
    ("2D","2D")
]

edadFuncionChoice=[
    ("mayor de edad","+18"),
    ("TE","Todo espectador"),
    ("mayor de 14","14")
]

inclusividad=[
    ("si","Si"),
    ("no","No"),
]

tiposalaChoice=[
    ("normal","Normal"),
    ("premium","Premium"),
    ("vip","Vip")
]
estadosalaChoice=[
    ("disponible","Disponible"),
    ("ocupado","Ocupado"),
]

tamanioPantallaChoice = [
    ("50","50"),
    ("55","55"),
    ("60","60"),
    ("65","65"),
    ("70","70"),
    ("80","80"),
]

class Cine(models.Model):
    id=models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=20)
    ubicacion = models.CharField(max_length=20)
    correo = models.EmailField(max_length=30)
    telefono = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return self.nombre
    

class Sala(models.Model):
    id=models.IntegerField(primary_key=True)
    CantidadSilla=models.PositiveIntegerField(default=0)
    NumeroSala=models.IntegerField(default=0)
    TamanioPantalla=models.CharField(max_length=10, choices=tamanioPantallaChoice)
    InclusividadSala=models.CharField(max_length=4, choices= inclusividad)
    TipoSala=models.CharField(max_length=10,choices=tiposalaChoice)
    EstadoSala=models.CharField(max_length=10,choices=estadosalaChoice)
    cine = models.CharField(max_length=30)

    def __str__(self) -> str:
        return f'{self.NumeroSala}'


class Funcion(models.Model):
    id=models.IntegerField(primary_key=True)
    duracionFuncion = models.CharField(max_length=20)
    nombreFuncion = models.CharField(max_length=20)
    horarioFuncion= models.CharField(max_length=30)
    tipoFuncion = models.CharField(max_length=10, choices= tipoFuncionChoice)
    generoFuncion = models.CharField(max_length=30)
    restriccionEdad = models.CharField(max_length=30, choices=edadFuncionChoice)
    sala = models.CharField(max_length=30)
    
    def __str__(self) -> str:
        return f'{self.NumeroSala},{self.horarioFuncion}'