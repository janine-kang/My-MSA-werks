from django.urls import path, include
from api.views import ITnewsViewSet, EconomyViewSet

app_name = 'api'

itnews_list = ITnewsViewSet.as_view({'get':'list'})
itnews_detail = ITnewsViewSet.as_view({'get':'retrieve'})

ecnews_list = EconomyViewSet.as_view({'get':'list'})
ecnews_detail = EconomyViewSet.as_view({'get':'retrieve'})


urlpatterns = [
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('its/', itnews_list, name='itnews_list'),
    path('its/<int:pk>', itnews_detail, name='itnews_detail'),

    path('economys/', ecnews_list, name='ecnews_list'),
    path('economys/<int:pk>', ecnews_detail, name='ecnews_detail'),
]