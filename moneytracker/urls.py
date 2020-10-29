from django.urls import path
from . import views
from moneytracker.views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='moneytracker'),
    path('investments', views.investments, name='investments'),
]
