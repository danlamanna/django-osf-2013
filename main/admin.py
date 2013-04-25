from django.contrib import admin
from main.models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'completed')

admin.site.register(Task, TaskAdmin)
