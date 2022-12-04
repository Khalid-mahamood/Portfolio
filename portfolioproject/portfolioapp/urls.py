from django.urls import path
from . import views

app_name = 'portfolioapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('Feedback/',views.reg,name='feedback')
    ]