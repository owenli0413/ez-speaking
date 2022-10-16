from django.contrib import admin
from . import models

class MessagesAdmin(admin.ModelAdmin):
    list_display = ('name','email','subject')

admin.site.register(models.Messages, MessagesAdmin)
