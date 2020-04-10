from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from events.views import Events


urlpatterns = [
    path('', include('frontend.urls')),
    path('admin/', admin.site.urls),
    path('', include('fridges.urls')),
    url(r'^events/', Events.as_view()),
]
