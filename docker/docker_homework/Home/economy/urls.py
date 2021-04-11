from django.conf.urls import url
from django.urls import path

from economy.views import EconomyLV, EconomyDV, EconomySearchFormView

app_name = 'economy'

urlpatterns = [

    path('', EconomyLV.as_view(), name='e_index'),    
    path('<int:pk>', EconomyDV.as_view(), name='e_detail'),
    path('search/economy/', EconomySearchFormView.as_view(), name='e_search'),
    # path('refresh', RefreshFormView.as_view(), name='e_refresh'),

]


