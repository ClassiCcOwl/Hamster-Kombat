from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from core_apps.game.models import Category, Card
from core_apps.game.services.categories import create_category
from core_apps.game.services.cards import create_card
from core_apps.game.selectors.cards import (
    get_single_card,
)
from core_apps.game.selectors.categories import (
    get_all_categories,
    get_single_categories_cards,
)
from drf_yasg.utils import swagger_auto_schema


class AllCategoriesApi(APIView):

    class CategoryCreateInputSerializer(serializers.Serializer):
        name = serializers.CharField(max_length=30)

    class AllCategoriesOutPutSerializer(serializers.ModelSerializer):
        cards_count = serializers.SerializerMethodField()

        class Meta:
            model = Category
            fields = [
                "name",
                "cards_count",
            ]

        def get_cards_count(self, obj):
            return obj.cards.count()

    @swagger_auto_schema(
        responses={200: AllCategoriesOutPutSerializer(many=True)},
    )
    def get(self, request):
        query = get_all_categories()

        return Response(
            self.AllCategoriesOutPutSerializer(
                query, context={"request": request}, many=True
            ).data
        )

    @swagger_auto_schema(
        request_body=CategoryCreateInputSerializer,
        responses={200: AllCategoriesOutPutSerializer(many=True)},
    )
    def post(self, request):
        serializer = self.CategoryCreateInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            query = create_category(name=serializer.validated_data.get("name"))
        except Exception as ex:
            return Response(str(ex), status=status.HTTP_400_BAD_REQUEST)

        return Response(
            self.AllCategoriesOutPutSerializer(query, context={"request": request}).data
        )


class SingleCategoryCardsApi(APIView):

    class SingleCategoryCardsOutPutSerializer(serializers.ModelSerializer):
        class Meta:
            model = Card
            fields = [
                "id",
                "name",
                "slug",
                "updated_at",
            ]

    @swagger_auto_schema(
        responses={200: SingleCategoryCardsOutPutSerializer(many=True)},
    )
    def get(self, request, category):
        query = get_single_categories_cards(category)

        return Response(
            self.SingleCategoryCardsOutPutSerializer(
                query, context={"request": request}, many=True
            ).data
        )
