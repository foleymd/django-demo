from django.urls import path
from . import views
from moneytracker.views import HomePageView

urlpatterns = [
    path('index', HomePageView.as_view(), name='index'),
    path('plotly', views.plotly, name='plotly'),
]
