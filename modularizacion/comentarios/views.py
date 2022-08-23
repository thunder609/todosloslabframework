from tokenize import Comment
from django.http import HttpResponse
from django.shortcuts import render
from .models import Comnents
# Create your views here.
def test(request):
     return HttpResponse("funciona correctamente")
def create(request):
  #  comment =Comnents(name="Juan",score=4, comment="este es un comentaro")
   # comment.save()
   comment =Comment.objects.create(name="Alex")
   return HttpResponse("ruta para crear modelos")  
def delete(request):
   # comment = Comment.objects.get(id=1)
   # comment.delete()
   Comnents.objects.filter(id=2).delete()
   return HttpResponse("ruta para borrar")