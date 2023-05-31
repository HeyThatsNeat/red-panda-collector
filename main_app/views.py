from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import RedPanda, Toy
from .forms import FeedingForm

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
  toys_red_panda_doesnt_have = Toy.objects.exclude(id__in = red_panda.toys.all().values_list('id'))
  feeding_form = FeedingForm()
  return render(request, 'red-pandas/detail.html', {
    'red_panda': red_panda, 'feeding_form': feeding_form, 'toys': toys_red_panda_doesnt_have
  })

def add_feeding(request, red_panda_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.red_panda_id = red_panda_id
    new_feeding.save()
  return redirect('red-panda-detail', red_panda_id=red_panda_id)

def assoc_toy(request, red_panda_id, toy_id):
  RedPanda.objects.get(id=red_panda_id).toys.add(toy_id)
  return redirect('red-panda-detail', red_panda_id=red_panda_id)

class RedPandaCreate(CreateView):
  model = RedPanda
  fields = '__all__'
  success_url = '/red-pandas/'

class RedPandaUpdate(UpdateView):
  model = RedPanda
  fields = ['name', 'breed', 'description', 'age']

class RedPandaDelete(DeleteView):
  model = RedPanda
  success_url = '/red-pandas/'

class ToyCreate(CreateView):
  model = Toy
  fields = '__all__'

class ToyList(ListView):
  model = Toy

class ToyDetail(DetailView):
  model = Toy

class ToyUpdate(UpdateView):
  model = Toy
  fields = ['name', 'color']

class ToyDelete(DeleteView):
  model = Toy
  success_url = '/toys/'