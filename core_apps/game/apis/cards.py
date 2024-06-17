from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from core_apps.game.models import Card
from core_apps.game.services.cards import create_card
from core_apps.game.selectors.cards import get_card, get_cards
from drf_yasg.utils import swagger_auto_schema


class CardsApi(APIView):
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
        query = get_cards()
        return Response(
            self.CardsOutPutSerializer(
                query, context={"request": request}, many=True
            ).data
        )


class CardApi(APIView):

    class CardInputSerializer(serializers.Serializer):
        category = serializers.CharField(max_length=30)

    class CardCreateInputSerializer(serializers.Serializer):
        name = serializers.CharField(max_length=50)
        # TODO: fix image
        image = serializers.SerializerMethodField()

    class CardOutPutSerializer(serializers.ModelSerializer):
        category = serializers.CharField(source="category.name")

        class Meta:
            model = Card
            fields = [
                "name",
                "category",
                "slug",
            ]

    @swagger_auto_schema(responses={200: CardOutPutSerializer(many=True)})
    def get(self, request, category):
        query = get_card(category=category)
        return Response(
            self.CardOutPutSerializer(
                query, context={"request": request}, many=True
            ).data
        )

    @swagger_auto_schema(
        request_body=CardCreateInputSerializer,
        responses={200: CardOutPutSerializer(many=True)},
    )
    def post(self, request, category):
        serializer = self.CardCreateInputSerializer(data=request.data)
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
            self.CardOutPutSerializer(query, context={"request": request}).data
        )
