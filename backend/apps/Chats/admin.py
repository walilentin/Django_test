from django.contrib import admin
from .models import Thread, Message

admin.site.register(Message)
admin.site.register(Thread)
