from rest_framework import serializers
from itnews.models import IT_news
from economy.models import EconomyNews

class ITnewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = IT_news
        fields = ['id', 'title', 'summary', 'paper']

class EconomySerializer(serializers.ModelSerializer):
    class Meta:
        model = EconomyNews
        fields = ['id', 'title', 'summary', 'paper']