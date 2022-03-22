from django.urls import path

from calculator import views

urlpatterns = [
    path('add/<int:first_num>/<int:second_num>/', views.add, name='add')
    path('substract/<int:first_num>/<int:second_num>/', views.substract, name='substract')
]