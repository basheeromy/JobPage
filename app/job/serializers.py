from rest_framework import serializers
from .models import (
    Job,
    CandidateApplied
)


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'


class JobApplicationSerializer(serializers.ModelSerializer):
    job = JobSerializer

    class Meta:
        model = CandidateApplied
        fields = ('user', 'resume', 'appliedAt', 'job')
