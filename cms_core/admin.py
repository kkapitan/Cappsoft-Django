from django.contrib import admin
from .models import Post, Service, Project


class ServiceAdmin(admin.ModelAdmin):
    model = Service
    list_display = ['name']


class ProjectAdmin(admin.ModelAdmin):
    model = Project
    list_display = ['title', 'description', 'client', 'finished_date', 'get_service']

    def get_service(self, obj):
        return obj.service.name
    get_service.short_description = 'Service'

admin.site.register(Post)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Project, ProjectAdmin)
