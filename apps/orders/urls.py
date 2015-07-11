from django.conf.urls import patterns, url, include
from .views import OrderViewSet
from rest_framework_nested import routers

router = routers.SimpleRouter()
router.register('orders', OrderViewSet, base_name='orders')

urlpatterns = patterns('',
    url(r'^api/', include(router.urls)),
)
