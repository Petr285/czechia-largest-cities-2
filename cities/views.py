from django.shortcuts import render, get_object_or_404
from .models import City

def city_list(request):
    cities = City.objects.all()
    return render(request, "cities/list.html", {"cities": cities})

def city_detail(request, pk):
    city = get_object_or_404(City, pk=pk)
    return render(request, "cities/detail.html", {"city": city})