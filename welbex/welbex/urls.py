from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from cargo.views import CargoViewSet
from car.views import CarViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
]

router = DefaultRouter()
router.register(r'cargo', CargoViewSet, basename='cargo')
router.register(r'car', CarViewSet, basename='car')

urlpatterns += router.urls
