"""
    Serializers for user API views.
"""

from django.contrib.auth import (get_user_model)

from rest_framework import serializers

from .models import UserProfile


class UserSerializer(serializers.ModelSerializer):

    resume = serializers.CharField(source='userprofile.resume', read_only=True)
    class Meta:
        model = get_user_model()
        fields = ['id','first_name','last_name','email', 'mobile','resume', 'password']
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}

    def create(self, validated_data):
        """Create and return a user with encrypted password."""

        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        """Handle updating user."""

        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)


class GenerateTokenSerializer(serializers.Serializer):
    """
    Serializer to take input for generating token.
    """
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        email = data['email']
        password = data['password']
        if not email:
            raise serializers.ValidationError("Email is required.")
        elif not password:
            raise serializers.ValidationError("Password is required.")

        user = get_user_model().objects.filter(email__iexact=email)

        if not user.exists():
            raise serializers.ValidationError("User not found! Please register.")
        user = user.first()
        if user.check_password(password) == False:
            raise serializers.ValidationError("Incorrect Password.")
        if user.is_active == False:
            raise serializers.ValidationError(
                "user not activated."
            )

        return user


class UploadResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('resume',)

    def validate_resume(self, file):
        """
            validate input data.
        """
        if file.content_type == "application/pdf":
            return file
        raise serializers.ValidationError("Invalid input.")
