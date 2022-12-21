from contextlib import _RedirectStream
from django.shortcuts import render, redirect
from .Serialiazers import ParticipanteSerializer
from .models import Participante
from serialApp.forms import FormParticipante
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404

# Create your views here.
class AñadirParticipante(APIView):

    def get(self, request):
        estu = Participante.objects.all()
        serial = ParticipanteSerializer(estu, many=True)
        return Response(serial.data)

    def post(self, request):
        serial = ParticipanteSerializer(data = request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
    
class DetalleParticipante(APIView):

    def get_object(self, pk):
        try:
            return Participante.objects.get(pk=pk)
        except Participante.DoesNotExist:
            return Http404
        
    def get(self, request, pk):
        estu = self.get_object(pk)
        serial = ParticipanteSerializer(estu)
        return Response(serial.data)

    def put(self, request, pk):
        estu = self.get_object(pk)
        serial = ParticipanteSerializer(estu, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        estu = self.get_object(pk)
        estu.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

def listaparticipante(request):
    perso = Participante.objects.all()
    data = {'participante': perso}
    return render(request, 'participantes.html', data)

def index(request):
    return render(request, 'index.html')

def listarparticipante(request):
    pro = Participante.objects.all()
    data = {'Participante': pro}
    return render(request, 'listarparticipante.html', data)

def agregarparticipante(request):
    form = FormParticipante()
    if request.method == 'POST':
        form = FormParticipante(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'añadirparticipante.html', data)

def actualizarParticipante(request, id):
    pro = Participante.objects.get(id = id)
    form = FormParticipante(instance=pro)
    if request.method == 'POST':
        form = FormParticipante(request.POST, instance=pro)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form': form}
    return render(request, 'agregarparticipante.html', data)


def eliminarParticipante(request, id):
    pro = Participante.objects.get(id = id)
    pro.delete()
    return redirect('/participante')




# Create your views here.
