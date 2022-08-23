from http.client import HTTPResponse
from nntplib import ArticleInfo
from turtle import title
from django.shortcuts import render
from django.http import HttpResponse
from .models import Article, Publication

def create(request):
    art1 = Article(headline="Articulo 1")
    art1.save()
    art2 = Article(headline="Articulo 2")
    art2.save()
    art3 = Article(headline="Articulo 3")
    art3.save()
    pub1= Publication(title="Publications primera")
    pub1.save()
    pub2= Publication(title="Publications segunda")
    pub2.save()
    pub3= Publication(title="Publications tercera")
    pub3.save()
    pub4= Publication(title="Publications cuarta")
    pub4.save()
    pub5= Publication(title="Publications quinta")
    pub5.save()
    pub6= Publication(title="Publications sexta")
    pub6.save()
    pub7= Publication(title="Publications septima")
    pub7.save()
    art1.publications.add(pub1)
    art1.publications.add(pub2)
    art1.publications.add(pub3)
    art2.publications.add(pub4)
    art2.publications.add(pub5)
    art3.publications.add(pub6)
    art3.publications.add(pub7) 
    result = art1.publications.all()
   # remover una relacion 
   # #art1 = publications.remove(pub1)
  # pub1 = Article.objects.filter(id__gte=0)
  # result = pub1.delete()
    return  HttpResponse(result)

