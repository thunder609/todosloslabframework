
from django.shortcuts import render
from django.http import HttpResponse
from .models import Place,Restaurant

# Create your views here.
def create(request):
    place = Place(name="Caracas",address="calle Simon")
    place.save()

    restaurant =Restaurant(place=place, name="macsonals",numbers_of_employees=5)
    restaurant.save()
    return HttpResponse(restaurant.place.name)
