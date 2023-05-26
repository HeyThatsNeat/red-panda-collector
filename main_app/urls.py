from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('red-pandas/', views.red_panda_index, name='red_panda_index'),
]