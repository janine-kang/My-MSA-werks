from django.contrib import admin
from django.urls import path, include
from Home.views import HomeView



urlpatterns = [
    path('admin/', admin.site.urls),

    path('', HomeView.as_view(), name='home'),
    path('IT/', include('itnews.urls', namespace='itnews')), 
    path('economy/', include('economy.urls', namespace='economy')),
   
]

