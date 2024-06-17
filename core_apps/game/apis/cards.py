from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from core_apps.game.models import Card
from core_apps.game.services.cards import create_card
from core_apps.game.selectors.cards import (
    get_single_card,
    get_all_cards,
)
from drf_yasg.utils import swagger_auto_schema


class AllCardsApi(APIView):

    class CardCreateInputSerializer(serializers.Serializer):
        name = serializers.CharField(max_length=50)
        category = serializers.CharField(max_length=30)
        # TODO: fix image
        image = serializers.SerializerMethodField()

    class CardsOutPutSerializer(serializers.ModelSerializer):
        category = serializers.CharField(source="category.name")

        class Meta:
            model = Card
            fields = [
                "name",
                "category",
                "slug",
            ]

    @swagger_auto_schema(
        responses={200: CardsOutPutSerializer(many=True)},
    )
    def get(self, request):
        cards = get_all_cards()
        return Response(
            self.CardsOutPutSerializer(
                cards,
                context={"request": request},
                many=True,
            ).data,
        )

    @swagger_auto_schema(
        request_body=CardCreateInputSerializer,
        responses={200: CardsOutPutSerializer},
    )
    def post(self, request):
        serializer = self.CardCreateInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            query = create_card(
                category=serializer.validated_data.get("category"),
                name=serializer.validated_data.get("name"),
                image=serializer.validated_data.get("image"),
            )

        except Exception as ex:
            return Response(str(ex), status=status.HTTP_400_BAD_REQUEST)
        return Response(
            self.CardsOutPutSerializer(query, context={"request": request}).data
        )


class SingleCardApi(APIView):

    class SingleCardOutPutSerializer(serializers.ModelSerializer):
        category = serializers.CharField(source="category.name")
        levels = serializers.SerializerMethodField()

        # TODO: add levels
        class Meta:
            model = Card
            fields = ["name", "category", "slug", "levels"]

        def get_levels(self, obj):
            return obj.levels.values(
                "level", "upgrade_cost", "profit_per_hour", "coin_per_profit"
            )

    @swagger_auto_schema(responses={200: SingleCardOutPutSerializer()})
    def get(self, request, slug):
        card = get_single_card(slug)
        return Response(
            self.SingleCardOutPutSerializer(card, context={"request": request}).data
        )
