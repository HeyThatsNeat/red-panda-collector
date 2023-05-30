from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('red-pandas/', views.red_panda_index, name='red_panda_index'),
  path('red-pandas/<int:red_panda_id>/', views.red_panda_detail, name='red-panda-detail'),
]