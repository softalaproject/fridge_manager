from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('frontend.urls')),
    path('admin/', admin.site.urls),
    path('', include('fridges.urls')),
    path('fridges/', include('api.urls')),
]
