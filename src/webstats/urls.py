from django.urls import path, include
from .views import HomePageView


urlpatterns = [
    path('', HomePageView, name='home' ),
]
