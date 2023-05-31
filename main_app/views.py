from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
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

class RedPandaCreate(CreateView):
  model = RedPanda
  fields = '__all__'
  success_url = '/red-pandas/'

class RedPandaUpdate(UpdateView):
  model = RedPanda
  fields = ['breed', 'description', 'age']

class RedPandaDelete(DeleteView):
  model = RedPanda
  success_url = '/red-pandas/'