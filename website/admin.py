from django.contrib import admin
from website.models import Project, Experience, Involvement

# Register your models here.

class ProjectsAdmin(admin.ModelAdmin):
  list_display=('title', 'technologies_used',)

class ExperienceAdmin(admin.ModelAdmin):
  list_display=('title',)
  list_filter=('title', 'description',)

class InvolvementsAdmin(admin.ModelAdmin):
  list_display=('title',)
  list_filter=('title', 'position',)

admin.site.register(Project, ProjectsAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Involvement, InvolvementsAdmin)




