from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

class RedPanda:
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

red_pandas = [
  RedPanda('Lolo', 'tabby', 'Kinda rude.', 3),
  RedPanda('Sachi', 'tortoiseshell', 'Looks like a turtle.', 0),
  RedPanda('Fancy', 'bombay', 'Happy fluff ball.', 4),
  RedPanda('Bonk', 'selkirk rex', 'Meows loudly.', 6)
]

# Add new view

def home(request):
  return HttpResponse('<h1>Hello</h1>')

def about(request):
  return render(request, 'about.html')

def red_panda_index(request):
  return render(request, 'red-pandas/index.html', { 'red_pandas': red_pandas })