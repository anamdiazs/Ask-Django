from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class Usuario(models.Model ):
    user = models.OneToOneField( User,on_delete=models.CASCADE  , unique= True)
    avatar = models.ImageField(upload_to='avatares/', null=True, blank= True)
    
    def __str__(self):
        return "{}" .format(self.user)
    
    
class Categories(models.Model):
    
    CIENCIA = 'ciencia'
    SALUD = 'salud'
    SOCIAL = 'social'
    RECETAS ='recetas'
    
    CATEGORIES = [
        (CIENCIA, 'ciencia'),
        (SALUD, 'salud'),
        (SOCIAL, 'social'),
        (RECETAS, 'recetas')  
    ]
    
    categories = models.CharField(max_length=20, choices=CATEGORIES,default=CIENCIA)
    def __str__(self):
        return "{}" .format(self.categories)
    
class create_question(models.Model):
    question = models.TextField(null= True, blank= True)
    categories =models.ForeignKey(Categories, on_delete=models.CASCADE)
    
    def __str__(self):
        return "{}" .format(self.question)
    
class create_answer(models.Model):
    question= models.ForeignKey(create_question,on_delete=models.CASCADE,null=True)
    answer = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return str(self.answer)

    
    

    
    
# Create your models here.
