from django.contrib import admin
from .models import info,  project


@admin.register(info)
class info_admin(admin.ModelAdmin):
	pass


@admin.register(project)
class project_admin(admin.ModelAdmin):
	pass
