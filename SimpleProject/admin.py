from django.contrib import admin
from django.db import models
from django import forms

from .models import Task

# Register your models here.

class TaskAdmin(admin.ModelAdmin):

    fieldsets = [
        (None, {'fields': ['task_title']}),
        ('Task Details', {'fields': ['task_description']}),
        (None, {'fields': ['deadline']}),
        (None, {'fields': ['groups']}),
        (None, {'fields': ['status']}),
        ]
    
    formfield_overrides = {
        models.CharField: {'widget': forms.Textarea}
        }
    
    list_display = ('task_id', 'task_title', 'start_date', 'deadline', 'groups', 'status')
    list_filter = [('deadline')]

    search_fields = ['task_title']

admin.site.register(Task, TaskAdmin)

