from rest_framework import serializers
from Cine.models import Cine
from Cine.models import Sala
from Cine.models import Funcion
class CineSerializer(serializers.Serializer):
    class Meta:
        model=Cine
        fields='__all__'

class SalaSerializer(serializers.Serializer):
    class Meta:
        model=Sala
        fields='__all__'

class FuncionSerializer(serializers.Serializer):
    class Meta:
        model=Funcion
        fields='__all__'