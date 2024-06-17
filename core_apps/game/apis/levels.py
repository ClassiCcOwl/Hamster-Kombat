from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from core_apps.game.models import Level
# from core_apps.game.services.levels import create_level
from core_apps.game.selectors.levels import (
    get_levels,
    # get_all_cards,
)
from drf_yasg.utils import swagger_auto_schema


class LevelApi(APIView):

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
