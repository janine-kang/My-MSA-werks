from rest_framework import viewsets
from rest_framework import permissions
from api.serializers import ITnewsSerializer, EconomySerializer
from itnews.models import IT_news
from economy.models import EconomyNews


class ITnewsViewSet(viewsets.ModelViewSet):
    queryset = IT_news.objects.all()
    serializer_class = ITnewsSerializer
    permission_classes = [permissions.IsAuthenticated]

class EconomyViewSet(viewsets.ModelViewSet):
    queryset = EconomyNews.objects.all()
    serializer_class = EconomySerializer
    permission_classes = [permissions.IsAuthenticated]