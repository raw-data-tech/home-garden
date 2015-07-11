from django.conf.urls import patterns, url, include
from .views import VegetableViewSet 
from rest_framework_nested import routers

router = routers.SimpleRouter()
router.register('vegetables', VegetableViewSet, base_name='vegetables')

urlpatterns = patterns('',
    url(r'^api/', include(router.urls)),
)


