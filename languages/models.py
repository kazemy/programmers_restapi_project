from django.db import models

#language table depend on Paradim table so we put
#Paradigh table above Languages table
class Paradigm(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Languages(models.Model):
    name = models.CharField(max_length=50)
    paradigm = models.ForeignKey(Paradigm, on_delete = models.CASCADE)

    def __str__(self):
        return self.name

class Programmer(models.Model):
    name = models.CharField(max_length=50)
    languages = models.ManyToManyField(Languages)
    
    def __str__(self):
        return self.name