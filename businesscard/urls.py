from django.urls import path

from businesscard import views

app_name = 'businesscard'

urlpatterns =[
    path('', views.businesscard, name='businesscard')
]