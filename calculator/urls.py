from django.urls import path

from calculator import views

urlpatterns = [
    path('add/<int:first_num>/<int:second_num>/', views.add, name='add'),
    path('subtract/<int:first_num>/<int:second_num>/', views.subtract, name='subtract'),
    path('multiply/<int:first_num>/<int:second_num>/', views.multiply, name='multiply'),
    path('divide/<int:first_num>/<int:second_num>/', views.divide, name='divide'),
]