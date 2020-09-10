from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Paradigm, Languages, Programmer
from .serializers import ParadigmSerializers, LanguageSerializers, ProgrammerSerializers

class ParadigmView(viewsets.ModelViewSet):
    queryset = Paradigm.objects.all()
    serializer_class = ParadigmSerializers
    #adding permission individually on Paradigm view
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

class LanguageView(viewsets.ModelViewSet):
    queryset = Languages.objects.all()
    serializer_class = LanguageSerializers

class ProgrammerView(viewsets.ModelViewSet):
    queryset = Programmer.objects.all()
    serializer_class = ProgrammerSerializers