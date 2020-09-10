from rest_framework import serializers
from .models import Languages, Paradigm, Programmer

class ParadigmSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Paradigm
        fields = ('id','url','name')

class LanguageSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Languages
        fields = ('id','url','name','paradigm')

class ProgrammerSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Programmer
        fields = ('id','url','name','languages')