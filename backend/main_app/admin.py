from django.contrib import admin

from .models import Todo

# Register your models here.
class TodoAdmin(admin.ModelAdmin):
 
    # add the fields of the model here
    list_display = ("title","description","completed")

admin.site.register(Todo,TodoAdmin)