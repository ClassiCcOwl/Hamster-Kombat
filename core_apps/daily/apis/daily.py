from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from core_apps.daily.models import DailyCombo
from core_apps.daily.services.daily import create_daily_combo
from core_apps.daily.selectors.daily import get_daily_combo, get_today_daily_combo
from drf_yasg.utils import swagger_auto_schema

from rest_framework.permissions import IsAuthenticatedOrReadOnly


class DailyCombosApi(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    class DailyComboOutPutSerializer(serializers.ModelSerializer):
        card_no_1 = serializers.SerializerMethodField()
        card_no_2 = serializers.SerializerMethodField()
        card_no_3 = serializers.SerializerMethodField()

        class Meta:
            model = DailyCombo
            fields = [
                "combo_date",
                "card_no_1",
                "card_no_2",
                "card_no_3",
            ]

        def get_card_no_1(self, obj):
            request = self.context.get("request")
            return {
                "name": obj.card_no_1.name,
                "image": request.build_absolute_uri(obj.card_no_1.image.url),
                "category": obj.card_no_1.category.name,
            }

        def get_card_no_2(self, obj):
            request = self.context.get("request")
            return {
                "name": obj.card_no_2.name,
                "image": request.build_absolute_uri(obj.card_no_2.image.url),
                "category": obj.card_no_2.category.name,
            }

        def get_card_no_3(self, obj):
            request = self.context.get("request")
            return {
                "name": obj.card_no_3.name,
                "image": request.build_absolute_uri(obj.card_no_3.image.url),
                "category": obj.card_no_3.category.name,
            }

    # class CardCreateInputSerializer(serializers.Serializer):
    #     name = serializers.CharField(max_length=50)
    #     category = serializers.CharField(max_length=30)
    #     # TODO: fix image
    #     image = serializers.SerializerMethodField()

    # class CardsOutPutSerializer(serializers.ModelSerializer):
    #     category = serializers.CharField(source="category.name")
    #     image = serializers.SerializerMethodField()
    #     levels = serializers.SerializerMethodField()

    #     class Meta:
    #         model = Card
    #         fields = ["name", "category", "slug", "image", "levels"]

    #     def get_levels(self, obj):
    #         return AllCardsApi.levelOutPutSerializer(obj.levels, many=True).data

    #     def get_image(self, obj):
    #         request = self.context.get("request")
    #         photo_url = obj.image.url
    #         return request.build_absolute_uri(photo_url)

    @swagger_auto_schema(
        responses={200: DailyComboOutPutSerializer},
    )
    def get(self, request, date):
        combo = get_daily_combo(date)
        return Response(
            self.DailyComboOutPutSerializer(
                combo,
                context={"request": request},
            ).data,
        )

    # @swagger_auto_schema(
    #     request_body=CardCreateInputSerializer,
    #     responses={200: CardsOutPutSerializer},
    # )
    # def post(self, request):
    #     serializer = self.CardCreateInputSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     try:
    #         query = create_card(
    #             category=serializer.validated_data.get("category"),
    #             name=serializer.validated_data.get("name"),
    #             image=serializer.validated_data.get("image"),
    #         )

    #     except Exception as ex:
    #         return Response(str(ex), status=status.HTTP_400_BAD_REQUEST)
    #     return Response(
    #         self.CardsOutPutSerializer(query, context={"request": request}).data
    #     )


class TodayCombosApi(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    @swagger_auto_schema(
        responses={200: DailyCombosApi.DailyComboOutPutSerializer},
    )
    def get(self, request):
        combo = get_today_daily_combo()
        return Response(
            DailyCombosApi.DailyComboOutPutSerializer(
                combo,
                context={"request": request},
            ).data,
        )
