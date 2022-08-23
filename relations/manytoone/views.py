import email
from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render
from .models import Report,Article
from datetime import date
# Create your views here.
def create(request):
    rep =Report(first_name='pedro',last_name="pepe", email='pedro@perdo.com')
    rep.save()
    art1 =Article(headline='ttttt', pub_date=date(2022,5,5),reporter=rep)
    art1.save()
    art2 =Article(headline='wwww', pub_date=date(2022,4,4),reporter=rep)
    art2.save()
    art3 =Article(headline='ttttr', pub_date=date(2022,9,9),reporter=rep)
    art3.save()   
    result =rep.article_set.count()
   # result = art1.reporter.first_name
    result =rep.article_set.all()
   # result =rep.article_set.filter(pub_date=date(2009,4,4))
    return HttpResponse(result)