
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers, serializers, viewsets
from api.views import RequestView, UserViewSet


# Routers provide a way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('items', RequestView.as_view(), name='item-list-create'),
]
