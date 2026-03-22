from django.urls import path
from . import views

urlpatterns = [
    path("", views.city_list),
    path("<int:pk>/", views.city_detail),
]