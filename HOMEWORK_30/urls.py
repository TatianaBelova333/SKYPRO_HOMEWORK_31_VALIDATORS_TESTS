from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.conf.urls.static import static
from HOMEWORK_30 import settings
from ads.views.location import LocationViewSet


router = routers.SimpleRouter()
router.register('location', LocationViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include('ads.urls')),
    path('user/', include('authentication.urls')),
]

urlpatterns += router.urls

if settings.DEBUG:
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)