from django.contrib import admin

# Register your models here.
from pim.models import ToDoItem

admin.site.register(ToDoItem)
