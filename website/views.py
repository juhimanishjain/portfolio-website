from django.shortcuts import render
from .models import Experience

# Create your views here.
def about_me(request):
  return render(request, "website/about_me.html")

def projects(request):
  return render(request, "website/projects.html")

def experiences(request):
  all_experiences=Experience.objects.all()
  return render(request, "website/experiences.html", {
    "experiences":all_experiences
  })

def recognition(request):
  return render(request, "website/recognition.html")

def achievements(request):
  return render(request, "website/achievements.html")

