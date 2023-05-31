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
  path('red-pandas/<int:red_panda_id>/add-feeding/', views.add_feeding, name='add-feeding'),
  path('red-pandas/<int:red_panda_id>/assoc-toy/<int:toy_id>/', views.assoc_toy, name='assoc-toy'),
  path('toys/create/', views.ToyCreate.as_view(), name='toy-create'),
  path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toy-detail'),
  path('toys/', views.ToyList.as_view(), name='toy-index'),
  path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toy-update'),
  path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toy-delete'),
]