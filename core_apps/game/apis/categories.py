from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from core_apps.game.models import Category
from core_apps.game.services.categories import create_category
from core_apps.game.selectors.categories import get_categories
from drf_yasg.utils import swagger_auto_schema


class CategoriesApi(APIView):

    class CategoryInputSerializer(serializers.Serializer):
        name = serializers.CharField(max_length=30)

    class CategoryOutPutSerializer(serializers.ModelSerializer):
        class Meta:
            model = Category
            fields = [
                "pkid",
                "id",
                "name",
                "created_at",
                "updated_at",
            ]

    @swagger_auto_schema(
        responses={200: CategoryOutPutSerializer(many=True)},
    )
    def get(self, request):
        query = get_categories()

        return Response(
            self.CategoryOutPutSerializer(
                query, context={"request": request}, many=True
            ).data
        )

    @swagger_auto_schema(
        request_body=CategoryInputSerializer,
        responses={200: CategoryOutPutSerializer(many=True)},
    )
    def post(self, request):
        serializer = self.CategoryInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            query = create_category(name=serializer.validated_data.get("name"))
        except Exception as ex:
            return Response(str(ex), status=status.HTTP_400_BAD_REQUEST)

        return Response(
            self.CategoryOutPutSerializer(query, context={"request": request}).data
        )
