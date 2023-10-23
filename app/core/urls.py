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
    ManageUserView
)

urlpatterns = [
    path('', CreatUserView.as_view(), name='create'),
    path('manage/', ManageUserView.as_view(), name="update"),
    path('token/', GenerateTokenView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]