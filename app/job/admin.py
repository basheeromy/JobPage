from django.contrib import admin


from .models import (
    Job,
    CandidateApplied
)

admin.site.register(Job)
admin.site.register(CandidateApplied)