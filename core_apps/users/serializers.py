from dj_rest_auth.registration.serializers import RegisterSerializer

from allauth.account.adapter import get_adapter
from rest_framework import serializers
from django.contrib.auth import get_user_model


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source="profile.first_name")
    last_name = serializers.CharField(source="profile.last_name")

    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name"]

    def to_representation(self, instance):
        representation = super(UserSerializer, self).to_representation(instance)
        if instance.is_superuser:
            representation["admin"] = True
        return representation


class CustomRegisterSerializer(RegisterSerializer):

    username = serializers.CharField(required=True)
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    email = None

    def get_cleaned_data(self):
        super().get_cleaned_data()

        return {
            "username": self.validated_data.get("username", ""),
            "password1": self.validated_data.get("password1", ""),
            "password2": self.validated_data.get("password2", ""),
            "email": "",
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        user = adapter.save_user(request, user, self)
        user.save()
        user.password = self.cleaned_data.get("password1")

        return user
