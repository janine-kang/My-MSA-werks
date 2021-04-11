from django.contrib import admin
from django.urls import path, include
from Home.views import HomeView



urlpatterns = [
    path('admin/', admin.site.urls),

    path('', HomeView.as_view(), name='home'),
    path('IT/', include('itnews.urls', namespace='itnews')), 
    path('economy/', include('economy.urls', namespace='economy')),
    path('api/', include('api.urls', namespace='api')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

