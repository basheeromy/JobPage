"""
    URL mapping for the user API.
"""

from django.urls import path

from rest_framework_simplejwt.views import (
    TokenRefreshView
)

from .views import (
    CreatUserView,
    GenerateTokenView,
    ManageUserView,
    ResumeView,
    AppliedJobListView
)

urlpatterns = [
    path('', CreatUserView.as_view(), name='create'),
    path('manage/', ManageUserView.as_view(), name="update"),
    path('token/', GenerateTokenView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('resume/', ResumeView.as_view(), name='upload_resume'),
    path('jobs-applied/', AppliedJobListView.as_view(), name='applied_jobs_list')
    # path('resume/', ManageResumeView.as_view(), name='manage_resume')
]