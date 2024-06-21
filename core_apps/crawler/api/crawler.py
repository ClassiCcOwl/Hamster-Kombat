from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from core_apps.crawler.services import crawlers
from core_apps.game.services.levels import create_level
from hamster_kombat.settings.base import env


class LevelApi(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        url = env("CRAWL_URL")
        categories = crawlers.crawl_categories(url)

        links = crawlers.get_links_from_category(categories)

        print("got links")

        for link in links.values():
            for card in link:

                print(card)
                levels = crawlers.crawl_level(card["link"])

                for level in levels:
                    try:
                        create_level(level[0], level[1], level[2], level[3])
                    except Exception as e:
                        print(e)
        # levels = crawlers.crawl_level()
        # for level in levels:
        return JsonResponse({"data": levels})
