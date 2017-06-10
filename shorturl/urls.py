from django.conf.urls import url, include
from shorturl import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'shorturls', views.ShortcutUrlsViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls'))
]