from django.contrib import admin
from django.urls import path,include

from post.views import *
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'messages', MessageViewSet)
router.register(r'parcels', ParcelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
