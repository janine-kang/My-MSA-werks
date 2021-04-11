from django.conf.urls import url
from django.urls import path

from itnews.views import BreakingsLV, BreakingsDV, SearchFormView, RefreshFormView

app_name = 'itnews'

urlpatterns = [

    path('', BreakingsLV.as_view(), name='index'),    
    path('<int:pk>', BreakingsDV.as_view(), name='detail'),
    path('search/IT/', SearchFormView.as_view(), name='search'),
    path('refresh', RefreshFormView.as_view(), name='refresh'),
]


