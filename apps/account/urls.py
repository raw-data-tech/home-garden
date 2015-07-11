from django.conf.urls import patterns, url, include
from rest_framework.authtoken import views
from .views import UserViewSet, ObtainAuthToken
from rest_framework_nested import routers

router = routers.SimpleRouter()
router.register('users', UserViewSet, base_name='users')

urlpatterns = patterns('',
    url(r'^api/', include(router.urls)),
    url(r'^api-auth-token/$', ObtainAuthToken.as_view()),
)
