from django.conf.urls import patterns, url, include
from .views import ListingViewSet
from rest_framework_nested import routers

router = routers.SimpleRouter()
router.register('listings', ListingViewSet, base_name='listings')

urlpatterns = patterns('',
    url(r'^api/', include(router.urls)),
)
