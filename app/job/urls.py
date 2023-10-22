from django.urls import path
from .views import (
    ListCreateJobView,
    ManageJobView,
    getTopicStats
)

urlpatterns = [
    path('jobs/', ListCreateJobView.as_view(), name='jobs'),
    path('jobs/<int:id>', ManageJobView.as_view(), name='manage_job'),
    path('stats/<str:topic>/', getTopicStats, name='get_topic_stats'),
]
