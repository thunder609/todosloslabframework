import email
from django.shortcuts import render
from django.http import  HttpResponse
from .models import Author,Entry

# Create your views here.
def queries(request):
    #obtener todos los elemtos
    authors=Author.objects.all()
   #obtener datos por condiciones
    filtered =Author.objects.filter(email='adriana71@example.net')
    #obtener un unico dato
    author =Author.objects.get(id=1)
      #obtener los primeros 10 elemtentos
    limit = Author.objects.all()[:10]
    #obtener los dies valores slatando los 5 primeros
    offsets =Author.objects.all()[5:15]
    #obtener los autores ordenados por email
    orders=Author.objects.all().order_by('email')
    #obtener todos los elementos cuyo id sea menor o igual a 15
    filtereds2=Author.objects.filter(id__lte=15)
    #obtener todos los autores que contienen yes
    namefilter=Author.objects.filter(name__contains="yes")
    return render(request,'post/queries.html',{'authors':authors,'filtered':filtered, 'author':author,'limit':limit,'offsets':offsets,'orders':orders,'filtereds2':filtereds2,"namefilter":namefilter})
def update(request):
    author=Author.objects.get(id=1)
    author.name="pedro jose"
    author.email="pedrojose@gmail.com"
    author.save()
    return HttpResponse("Modificado")
  
