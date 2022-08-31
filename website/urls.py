from django.urls import path
from . import views


urlpatterns = [
    path("about-me", views.about_me, name="about-me"),
    path("projects", views.projects, name="projects"),
    path("experiences", views.experiences, name="experiences"),
    path("recognition", views.recognition, name="recognition"),
    path("achievements", views.achievements, name="achievements")
]
