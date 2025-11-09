from django.contrib import admin
from django.contrib.admin.options import InlineModelAdmin

from main.models import *
from django.contrib.auth.models import User, Group
admin.site.unregister(Group)
admin.site.unregister(User)

class IncorrectInline(admin.StackedInline):
    model = Incorrect
    extra = 1

@admin.register(Correct)
class CorrectAdmin(admin.ModelAdmin):
    inlines = [IncorrectInline]

@admin.register(Incorrect)
class IncorrectAdmin(admin.ModelAdmin):
    pass