from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from core_apps.game.models import Card, Level
from core_apps.game.services.cards import create_card
from core_apps.game.selectors.cards import (
    get_single_card,
    get_all_cards,
    get_recently_added_cards,
)
from drf_yasg.utils import swagger_auto_schema

from rest_framework.permissions import IsAuthenticatedOrReadOnly


class AllCardsApi(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    class levelOutPutSerializer(serializers.ModelSerializer):

        class Meta:
            model = Level
            fields = [
                "level",
                "upgrade_cost",
                "profit_per_hour",
                "coin_per_profit",
            ]

    class CardCreateInputSerializer(serializers.Serializer):
        name = serializers.CharField(max_length=50)
        category = serializers.CharField(max_length=30)
        # TODO: fix image
        image = serializers.SerializerMethodField()

    class CardsOutPutSerializer(serializers.ModelSerializer):
        category = serializers.CharField(source="category.name")
        image = serializers.SerializerMethodField()
        levels = serializers.SerializerMethodField()

        class Meta:
            model = Card
            fields = [
                "id",
                "name",
                "category",
                "slug",
                "image",
                "levels",
            ]

        def get_levels(self, obj):
            return AllCardsApi.levelOutPutSerializer(obj.levels, many=True).data

        def get_image(self, obj):
            request = self.context.get("request")
            photo_url = obj.image.url
            photo_uri = request.build_absolute_uri(photo_url)
            photo_uri_secured = photo_uri.replace("http", "https")
            return photo_uri_secured

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
    permission_classes = [IsAuthenticatedOrReadOnly]

    class SingleCardOutPutSerializer(serializers.ModelSerializer):
        category = serializers.CharField(source="category.name")
        levels = serializers.SerializerMethodField()
        image = serializers.SerializerMethodField()

        # TODO: add levels
        class Meta:
            model = Card
            fields = [
                "id",
                "name",
                "category",
                "slug",
                "levels",
                "image",
            ]

        def get_levels(self, obj):
            return AllCardsApi.levelOutPutSerializer(obj.levels, many=True).data

        def get_image(self, obj):
            request = self.context.get("request")
            photo_url = obj.image.url
            photo_uri = request.build_absolute_uri(photo_url)
            photo_uri_secured = photo_uri.replace("http", "https")
            return photo_uri_secured

    @swagger_auto_schema(responses={200: SingleCardOutPutSerializer()})
    def get(self, request, slug):
        card = get_single_card(slug)
        return Response(
            self.SingleCardOutPutSerializer(card, context={"request": request}).data
        )


class RecentlyAddedCardsApi(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    class RecantlyAddedCardsOutPutSerializer(serializers.ModelSerializer):
        category = serializers.CharField(source="category.name")
        image = serializers.SerializerMethodField()

        class Meta:
            model = Card
            fields = [
                "id",
                "name",
                "category",
                "slug",
                "image",
            ]

        def get_image(self, obj):
            request = self.context.get("request")
            photo_url = obj.image.url
            photo_uri = request.build_absolute_uri(photo_url)
            photo_uri_secured = photo_uri.replace("http", "https")
            return photo_uri_secured

    @swagger_auto_schema(responses={200: RecantlyAddedCardsOutPutSerializer(many=True)})
    def get(self, request, number):
        card = get_recently_added_cards(number)
        return Response(
            self.RecantlyAddedCardsOutPutSerializer(
                card,
                context={"request": request},
                many=True,
            ).data
        )
