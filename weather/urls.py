from django.urls import path
from . import views
from weather.views import HomePageView, CurrentView

urlpatterns = [
    path('', HomePageView.as_view(), name='weather'),
    path('current', CurrentView.as_view(), name='current'),

]
