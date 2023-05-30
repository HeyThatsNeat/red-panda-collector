from django.shortcuts import render
from .models import RedPanda

# Add new view

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def red_panda_index(request):
  red_pandas = RedPanda.objects.all()
  return render(request, 'red-pandas/index.html', { 'red_pandas': red_pandas })

def red_panda_detail(request, red_panda_id):
  red_panda = RedPanda.objects.get(id=red_panda_id)
  return render(request, 'red-pandas/detail.html', { 'red_panda': red_panda })