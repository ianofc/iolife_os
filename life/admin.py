from django.contrib import admin
from .models import LifeDimension, Milestone, JournalEntry, Goal
admin.site.register(LifeDimension)
admin.site.register(Milestone)
admin.site.register(JournalEntry)
admin.site.register(Goal)