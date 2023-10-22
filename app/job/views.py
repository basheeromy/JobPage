"""
    Views to handle jobs
"""

from django.shortcuts import get_object_or_404

from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)

from .serializers import JobSerializer
from .models import Job


class ListCreateJobView(ListCreateAPIView):
    """
    View to create and list all jobs.
    """
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class ManageJobView(RetrieveUpdateDestroyAPIView):
    """
    Manage jobs.
    get, put, patch, delete methods
    """

    serializer_class = JobSerializer
    queryset = Job.objects.all()
    lookup_field = 'id'

    def get_object(self):
        obj = get_object_or_404(
            self.get_queryset(),
            pk=self.kwargs["id"]
        )
        return obj
