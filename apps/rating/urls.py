from django.conf.urls import patterns, url, include
from rest_framework_nested import routers
from .views import RatingViewSet

router = routers.SimpleRouter()
router.register('rating',RatingViewSet,base_name='rating')


urlpatterns = patterns('',
    url(r'^api/', include(router.urls)),
)
