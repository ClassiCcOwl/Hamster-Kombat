from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from core_apps.profiles.models import Profile, ProfileCard
from ..selectors.profile import get_profile
from ..selectors.profile_cards import get_profile_cards
from ..services.profile_cards import create_or_update_profile_card
from core_apps.game.selectors.cards import get_single_card_by_id


from drf_yasg.utils import swagger_auto_schema

from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated


class ProfileAddCard(APIView):
    permission_classes = [IsAuthenticated]

    class profileCardSerializer(serializers.ModelSerializer):
        card = serializers.CharField(source="card.name")
        profit_per_hour = serializers.IntegerField(
            source="related_level.profit_per_hour"
        )
        upgrade_cost = serializers.IntegerField(source="related_level.upgrade_cost")
        coin_per_profit = serializers.IntegerField(
            source="related_level.coin_per_profit"
        )

        class Meta:
            model = ProfileCard
            fields = [
                "card",
                "level",
                "upgrade_cost",
                "profit_per_hour",
                "coin_per_profit",
            ]

    @swagger_auto_schema(
        responses={200: profileCardSerializer},
    )
    def post(self, request, card_id, level: int):
        user = request.user
        user_profile = get_profile(user)
        print(user_profile)
        selected_card = get_single_card_by_id(card_id)
        print(type(selected_card))
        profile_card = create_or_update_profile_card(
            profile=user_profile, card=selected_card, level=level
        )

        print(profile_card)
        return Response(
            self.profileCardSerializer(
                profile_card,
                context={"request": request},
            ).data,
        )


class ProfileCards(APIView):
    permission_classes = [IsAuthenticated]

    class profileCardsSerializer(serializers.ModelSerializer):
        card = serializers.CharField(source="card.name")
        profit_per_hour = serializers.IntegerField(
            source="related_level.profit_per_hour"
        )
        upgrade_cost = serializers.IntegerField(source="related_level.upgrade_cost")
        coin_per_profit = serializers.IntegerField(
            source="related_level.coin_per_profit"
        )
        card_id = serializers.CharField(source="card.id")

        class Meta:
            model = ProfileCard
            fields = [
                "card_id",
                "card",
                "level",
                "upgrade_cost",
                "profit_per_hour",
                "coin_per_profit",
            ]

    @swagger_auto_schema(
        responses={200: profileCardsSerializer(many=True)},
    )
    def get(self, request):
        user = request.user
        user_profile = get_profile(user)
        profile_cards = get_profile_cards(user_profile)
        return Response(
            self.profileCardsSerializer(
                profile_cards,
                context={"request": request},
                many=True,
            ).data,
        )
