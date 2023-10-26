"""
    Views to handle jobs
"""
from django.shortcuts import get_object_or_404
from django.db.models import Min, Max, Avg, Count
from django.utils import timezone

from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    CreateAPIView
)
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import permissions

from permissions import custom_permissions
from .serializers import (
    JobSerializer
)
from .models import (
    Job,
    CandidateApplied
)
from .filters import JobsFilter
from .paginations import CustomPagination


class ListCreateJobView(ListCreateAPIView):
    """
    View to create and list all jobs.
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    filterset_class = JobsFilter
    pagination_class = CustomPagination

    def perform_create(self, serializer):
        """
        perform_create method will help us to
        assign request.user to user field of job model
        before create method is called.
        """
        serializer.save(user=self.request.user)


class ManageJobView(RetrieveUpdateDestroyAPIView):
    """
    Manage jobs.
    get, put, patch, delete methods
    """

    authentication_classes = [JWTAuthentication]
    permission_classes = [
        permissions.IsAuthenticated,
        custom_permissions.IsOwnerOrReadOnly
    ]
    serializer_class = JobSerializer
    queryset = Job.objects.all()
    lookup_field = 'id'

    def get_object(self):
        obj = get_object_or_404(
            self.get_queryset(),
            pk=self.kwargs["id"]
        )
        self.check_object_permissions(
            self.request,
            obj
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


class ApplyJobView(APIView):
    """
        View to handle job applications.
    """

    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, id):
        """
            Create new instance
        """
        user = request.user
        job = Job.objects.filter(pk = id).first()

        # find resume
        if hasattr(user, 'userprofile'):
            resume = user.userprofile.resume
        else:
            return Response(
                {'error': "No resume found, Please upload resume."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # additional verifications.
        if job.candidateapplied_set.filter(user=user).exists():
            return Response(
                {'error': "You have already applied for this job."},
                status=status.HTTP_400_BAD_REQUEST
            )

        if job.lastDate < timezone.now():
            return Response(
                {
                    'error':
                        "The application deadline has already passed."
                        " Applications are no longer being accepted."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        # create new jobapplication instance.
        job_applied = CandidateApplied.objects.create(
            job = job,
            user = user,
            resume = resume
        )

        return Response(
            {
                'applied': True,
                'application_id': job_applied.id
            },
            status=status.HTTP_201_CREATED
        )
