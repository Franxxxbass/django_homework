from django.urls import path

from monday import views


urlpatterns=[
    path('', views.monday, name='monday')
]