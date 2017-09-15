from django.contrib import admin
from vote.models import Vote

# Register your models here.
@admin.register(Vote)
class VoteModelAdmin(admin.ModelAdmin):
    pass