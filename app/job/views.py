"""
    Views to handle jobs
"""
from django.shortcuts import get_object_or_404
from django.db.models import Min, Max, Avg, Count

from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from rest_framework.decorators import api_view
from rest_framework.response import Response


from .serializers import JobSerializer
from .models import Job
from .filters import JobsFilter
from .paginations import CustomPagination


class ListCreateJobView(ListCreateAPIView):
    """
    View to create and list all jobs.
    """
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    filterset_class = JobsFilter
    pagination_class = CustomPagination


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

@api_view(['GET'])
def getTopicStats(request, topic):
    """
    get statics for search topics from database.
    """

    args = {'title__icontains': topic}
    jobs = Job.objects.filter(**args)
    print(jobs)
    if len(jobs) == 0:
        return Response({
            'message': f'No data found for {topic}'
        })

    stats = jobs.aggregate(
        total_jobs = Count('title'),
        avg_positions = Avg('positions'),
        avg_salary = Avg('salary'),
        min_salary = Min('salary'),
        max_salary = Max('salary')
    )

    return Response(stats)
