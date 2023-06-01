from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import RedPanda, Toy
from .forms import FeedingForm

# Add new view

class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

@login_required
def red_panda_index(request):
  red_pandas = RedPanda.objects.filter(user=request.user)
  return render(request, 'red-pandas/index.html', { 'red_pandas': red_pandas })

@login_required
def red_panda_detail(request, red_panda_id):
  red_panda = RedPanda.objects.get(id=red_panda_id)
  toys_red_panda_doesnt_have = Toy.objects.exclude(id__in = red_panda.toys.all().values_list('id'))
  feeding_form = FeedingForm()
  return render(request, 'red-pandas/detail.html', {
    'red_panda': red_panda, 'feeding_form': feeding_form, 'toys': toys_red_panda_doesnt_have
  })

@login_required
def add_feeding(request, red_panda_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.red_panda_id = red_panda_id
    new_feeding.save()
  return redirect('red-panda-detail', red_panda_id=red_panda_id)

@login_required
def assoc_toy(request, red_panda_id, toy_id):
  RedPanda.objects.get(id=red_panda_id).toys.add(toy_id)
  return redirect('red-panda-detail', red_panda_id=red_panda_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('red-panda-index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)

class RedPandaCreate(LoginRequiredMixin, CreateView):
  model = RedPanda
  fields = '__all__'
  success_url = '/red-pandas/'
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class RedPandaUpdate(LoginRequiredMixin, UpdateView):
  model = RedPanda
  fields = ['name', 'breed', 'description', 'age']

class RedPandaDelete(LoginRequiredMixin, DeleteView):
  model = RedPanda
  success_url = '/red-pandas/'

class ToyCreate(LoginRequiredMixin, CreateView):
  model = Toy
  fields = '__all__'

class ToyList(LoginRequiredMixin, ListView):
  model = Toy

class ToyDetail(LoginRequiredMixin, DetailView):
  model = Toy

class ToyUpdate(LoginRequiredMixin, UpdateView):
  model = Toy
  fields = ['name', 'color']

class ToyDelete(LoginRequiredMixin, DeleteView):
  model = Toy
  success_url = '/toys/'