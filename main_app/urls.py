from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('red-pandas/', views.red_panda_index, name='red-panda-index'),
  path('red-pandas/<int:red_panda_id>/', views.red_panda_detail, name='red-panda-detail'),
  path('red-pandas/create/', views.RedPandaCreate.as_view(), name='red-panda-create'),
  path('red-pandas/<int:pk>/update/', views.RedPandaUpdate.as_view(), name='red-panda-update'),
  path('red-pandas/<int:pk>/delete/', views.RedPandaDelete.as_view(), name='red-panda-delete'),
]