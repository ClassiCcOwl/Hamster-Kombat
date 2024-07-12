from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from core_apps.profiles.models import Profile, ProfileCard
from ..selectors.profile import get_profile


from drf_yasg.utils import swagger_auto_schema

from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated


class ProfileAPI(APIView):
    permission_classes = [IsAuthenticated]

    class profileSerializer(serializers.ModelSerializer):
        user = serializers.UUIDField(source="user.id")
        username = serializers.CharField(source="user.username")

        class Meta:
            model = Profile
            fields = ["user", "username", "first_name", "last_name"]

    @swagger_auto_schema(
        responses={200: profileSerializer},
    )
    def get(self, request):
        user = request.user
        user_profile = get_profile(user)

        return Response(
            self.profileSerializer(
                user_profile,
                context={"request": request},
            ).data,
        )
