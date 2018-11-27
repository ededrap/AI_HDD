from django.urls import path

from . import views

urlpatterns = [
    path(r'', views.get_name, name='get_name')
    #path('form/', views.get_name, name='get_name')
]