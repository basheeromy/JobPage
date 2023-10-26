"""Views for the Create user API"""

from django.shortcuts import get_object_or_404

from rest_framework import permissions
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView,
    ListCreateAPIView,
    CreateAPIView,
    DestroyAPIView,
    GenericAPIView
)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import (
    UserSerializer,
    GenerateTokenSerializer,
    UploadResumeSerializer
    )

from .models import UserProfile
from django.contrib.auth import get_user_model

from drf_spectacular.utils import extend_schema


class CreatUserView(ListCreateAPIView):
    """Create a new Customer user."""
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()


class ManageUserView(RetrieveUpdateDestroyAPIView):
    """Manage the authenticated user."""
    serializer_class = UserSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = get_user_model().objects.all()

    def get_object(self):
        return self.request.user


class GenerateTokenView(APIView):
    """
    View to generate token.
    """

    @extend_schema(request=GenerateTokenSerializer, responses=None)
    def post(self, request, *args, **kwargs):
        serializer = GenerateTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        refresh = RefreshToken.for_user(data)
        return Response({'refresh': str(refresh),
                         'access': str(refresh.access_token),
        })


class ResumeView(APIView):
    """
        View to handle resume .
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UploadResumeSerializer
    queryset = UserProfile.objects.all()


    def post(self,request):
        """
        Create new instance or edit excisting.
        """
        serializer = UploadResumeSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = request.user
            resume = request.data['resume']
            profile = UserProfile.objects.filter(user=user).first()
            if profile:
                profile.resume = resume
                profile.save()
            else:
                profile = UserProfile(
                    user = user,
                    resume = resume
                )
                profile.save()
                
            return Response(status=status.HTTP_201_CREATED)

    def delete(self,request):
        """
        delete userprofile instance.
        """
        user = request.user
        obj = get_object_or_404(
            UserProfile.objects.filter(user=user)
        )
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
