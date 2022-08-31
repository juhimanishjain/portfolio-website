from django.db import models

# Create your models here.

class Project(models.Model):
  image=models.ImageField(upload_to='website/static/images') 
  title=models.CharField(max_length=100) 
  technologies_used=models.CharField(max_length=100)
  description=models.CharField(max_length=200)
  github_link=models.URLField(max_length=300)

class Experience(models.Model):
  image=models.ImageField(upload_to='website/static/images') 
  title=models.CharField(max_length=100) 
  position=models.CharField(default="",max_length=150) 
  timeline=models.CharField(default="", max_length=50)
  description=models.CharField(max_length=500)





