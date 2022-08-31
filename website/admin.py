from django.contrib import admin
from website.models import Project, Experience

# Register your models here.

class ProjectsAdmin(admin.ModelAdmin):
  list_display=('title', 'technologies_used',)

class ExperienceAdmin(admin.ModelAdmin):
  list_display=('title',)
  list_filter=('title', 'description',)


admin.site.register(Project, ProjectsAdmin)
admin.site.register(Experience, ExperienceAdmin)





