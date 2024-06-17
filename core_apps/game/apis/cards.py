from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from core_apps.game.models import Card
from core_apps.game.services.cards import create_card
from core_apps.game.selectors.cards import (
    get_single_card,
    get_single_category_cards,
    get_all_categories_cards,
)
from drf_yasg.utils import swagger_auto_schema


class AllCategoriesCardsApi(APIView):
    class AllCategoryCardsOutPutSerializer(serializers.ModelSerializer):
        category = serializers.CharField(source="category.name")

        class Meta:
            model = Card
            fields = [
                "name",
                "category",
                "slug",
            ]

    @swagger_auto_schema(
        responses={200: AllCategoryCardsOutPutSerializer(many=True)},
    )
    def get(self, request):
        cards = get_all_categories_cards()
        return Response(
            self.AllCategoryCardsOutPutSerializer(
                cards, context={"request": request}, many=True
            ).data
        )


class SingleCategoryCardsApi(APIView):

    class SingleCategoryCardsCreateInputSerializer(serializers.Serializer):
        name = serializers.CharField(max_length=50)
        # TODO: fix image
        image = serializers.SerializerMethodField()

    class SingleCategoryCardsOutPutSerializer(serializers.ModelSerializer):
        category = serializers.CharField(source="category.name")

        class Meta:
            model = Card
            fields = [
                "name",
                "category",
                "slug",
            ]

    @swagger_auto_schema(
        responses={200: SingleCategoryCardsOutPutSerializer(many=True)}
    )
    def get(self, request, category):
        cards = get_single_category_cards(category=category)
        return Response(
            self.SingleCategoryCardsOutPutSerializer(
                cards, context={"request": request}, many=True
            ).data
        )

    @swagger_auto_schema(
        request_body=SingleCategoryCardsCreateInputSerializer,
        responses={200: SingleCategoryCardsOutPutSerializer(many=True)},
    )
    def post(self, request, category):
        serializer = self.SingleCategoryCardsCreateInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            query = create_card(
                category=category,
                name=serializer.validated_data.get("name"),
                image=serializer.validated_data.get("image"),
            )

        except Exception as ex:
            return Response(str(ex), status=status.HTTP_400_BAD_REQUEST)
        return Response(
            self.SingleCategoryCardsOutPutSerializer(
                query, context={"request": request}
            ).data
        )


class SingleCardApi(APIView):

    class SingleCardOutPutSerializer(serializers.ModelSerializer):
        category = serializers.CharField(source="category.name")
        levels = serializers.ListField(source='levels.level')

        # TODO: add levels
        class Meta:
            model = Card
            fields = [
                "name",
                "category",
                "slug",
                'levels'
            ]

    @swagger_auto_schema(responses={200: SingleCardOutPutSerializer()})
    def get(self, request, slug):
        card = get_single_card(slug)
        return Response(
            self.SingleCardOutPutSerializer(card, context={"request": request}).data
        )
