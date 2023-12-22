from django.shortcuts import render
from .serializers import SalaSerializer, FuncionSerializer, CineSerializer
from .models import Cine,Funcion,Sala
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import generics,mixins
from rest_framework import viewsets




class CineList(generics.ListCreateAPIView,mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Cine.objects.all()
    serializer_class = CineSerializer

    def get(self, request):
        cine = Cine.objects.all()
        serializer = CineSerializer(cine, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CineDetail(generics.RetrieveUpdateDestroyAPIView,mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Cine.objects.all()
    serializer_class = CineSerializer
    def get_object(self, pk):
        try: 
            return Cine.objects.get(pk=pk)
        except Cine.DoesNotExist:
            return Http404
    
    def get(self,request, pk):
        cine = self.get_object(pk)
        serializer = CineSerializer(cine)
        return Response(serializer.data)

    def put(self, request, pk):
        cine = self.get_object(pk)
        serializer = CineSerializer(cine, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        cine = self.get_object(pk)
        cine.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class FuncionList(generics.ListCreateAPIView,mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Funcion.objects.all()
    serializer_class = FuncionSerializer
    def get(self, request):
        funcion = Funcion.objects.all()
        serializer = FuncionSerializer(funcion, many=True)
        return Response(serializer.data)
    
class FuncionDetail(generics.RetrieveUpdateDestroyAPIView,mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Funcion.objects.all()
    serializer_class = FuncionSerializer

    def get_object(self, pk):
        try: 
            return Funcion.objects.get(pk=pk)
        except Funcion.DoesNotExist:
            return Http404
    
    def get(self,request, pk):
        funcion = self.get_object(pk)
        serializer = FuncionSerializer(funcion)
        return Response(serializer.data)

    def put(self, request, pk):
        funcion = self.get_object(pk)
        serializer = FuncionSerializer(funcion, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        funcion = self.get_object(pk)
        funcion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class SalaList(generics.ListCreateAPIView,mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Sala.objects.all()
    serializer_class = SalaSerializer
    def get(self, request):
        sala = Sala.objects.all()
        serializer = SalaSerializer(sala, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SalaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SalaDetail(generics.RetrieveUpdateDestroyAPIView,mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Sala.objects.all()
    serializer_class = SalaSerializer
    def get_object(self, pk):
        try: 
            return Sala.objects.get(pk=pk)
        except Sala.DoesNotExist:
            return Http404
    
    def get(self,request, pk):
        sala = self.get_object(pk)
        serializer = SalaSerializer(sala)
        return Response(serializer.data)

    def put(self, request, pk):
        sala = self.get_object(pk)
        serializer = SalaSerializer(sala, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        sala = self.get_object(pk)
        sala.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
