from django.contrib import admin
from .models import ToDoItem, SubItem


class ToDoAdmin(admin.ModelAdmin):
    list_display = ('user', 'text', 'urgency', 'date')
    ordering = ['user', 'date']


class SubItemAdmin(admin.ModelAdmin):
    list_display = ('item', 'text', 'date')
    ordering = ['item', 'date']


admin.site.register(ToDoItem, ToDoAdmin)
admin.site.register(SubItem, SubItemAdmin)
# Register your models here.
