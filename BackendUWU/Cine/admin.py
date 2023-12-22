from django.contrib import admin
from Cine.models import Cine
from Cine.models import Funcion
from Cine.models import Sala

class CineAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre','ubicacion','correo','telefono']
admin.site.register(Cine,CineAdmin)

class FuncionAdmin(admin.ModelAdmin):
    list_display = ['id','duracionFuncion','nombreFuncion','horarioFuncion','tipoFuncion','generoFuncion','restriccionEdad']
admin.site.register(Funcion,FuncionAdmin)

class SalaAdmin(admin.ModelAdmin):
    list_display = ['id','CantidadSilla','NumeroSala','TamanioPantalla','InclusividadSala','TipoSala','EstadoSala']

admin.site.register(Sala,SalaAdmin)