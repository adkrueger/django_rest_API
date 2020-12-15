from django.urls import path

from . import views

app_name = 'rest_API'
urlpatterns = [
    path('', views.index, name='index')
]
