from django.contrib import admin

from hospitalapp.models import Contact, Email

# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message')
    search_fields = ('name', 'email', 'subject')

@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
    list_display = ('email',)
    search_fields = ('email',)