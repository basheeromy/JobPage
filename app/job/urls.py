from django.urls import path
from .views import (
    ListCreateJobView,
    ManageJobView,
    ApplyJobView,
    getTopicStats,
    isApplied
)

urlpatterns = [
    path('jobs/', ListCreateJobView.as_view(), name='jobs'),
    path('jobs/<int:id>', ManageJobView.as_view(), name='manage_job'),
    path('stats/<str:topic>/', getTopicStats, name='get_topic_stats'),
    path('jobs/<int:id>/apply/', ApplyJobView.as_view(), name='apply_for_job'),
    path('jobs/<int:id>/check/', isApplied, name='is_applied_to_job'),
]
