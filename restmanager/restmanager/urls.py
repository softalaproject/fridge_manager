from django.contrib import admin
from django.urls import path, include
from fridges import urls


urlpatterns = [
    path('', include('frontend.urls')),
    path('admin/', admin.site.urls),
    path('', include('fridges.urls')),
]
