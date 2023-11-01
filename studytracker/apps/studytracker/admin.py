from django.contrib import admin
from .models import Project, ProjectMember, Note, Task
# Register your models here.

# class ProjectAdmin(admin.ModelAdmin):
#     # fields変数を設定する
#     fields = ['project_id', 'project_name', 'created_user']

admin.site.register(Project)
admin.site.register(ProjectMember)
admin.site.register(Note)
admin.site.register(Task)