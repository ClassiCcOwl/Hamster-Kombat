from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from core_apps.game.models import Level
from core_apps.game.services.levels import create_level
from core_apps.game.selectors.levels import (
    get_levels,
    # get_all_cards,
)
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class LevelApi(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    class LevelCreateInputSerializer(serializers.Serializer):
        level = serializers.IntegerField()
        upgrade_cost = serializers.IntegerField()
        profit_per_hour = serializers.IntegerField()

    class levelOutPutSerializer(serializers.ModelSerializer):

        class Meta:
            model = Level
            fields = [
                "level",
                "upgrade_cost",
                "profit_per_hour",
                "coin_per_profit",
            ]

    @swagger_auto_schema(
        responses={200: levelOutPutSerializer(many=True)},
    )
    def get(self, request, slug):
        levels = get_levels(slug)
        return Response(
            self.levelOutPutSerializer(
                levels,
                context={"request": request},
                many=True,
            ).data,
        )

    @swagger_auto_schema(
        request_body=LevelCreateInputSerializer,
        responses={200: levelOutPutSerializer(many=True)},
    )
    def post(self, request, slug):
        serializer = self.LevelCreateInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            query = create_level(
                level=serializer.validated_data.get("level"),
                upgrade_cost=serializer.validated_data.get("upgrade_cost"),
                profit_per_hour=serializer.validated_data.get("profit_per_hour"),
                slug=slug,
            )
        except Exception as ex:
            return Response(str(ex), status=status.HTTP_400_BAD_REQUEST)

        return Response(
            self.levelOutPutSerializer(query, context={"request": request}).data
        )
