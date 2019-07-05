from django.contrib import admin

# Register your models here.
from .models import Poll, Tag, Option

admin.site.register(Poll)
admin.site.register(Tag)
admin.site.register(Option)