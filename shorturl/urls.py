from django.conf.urls import url, include
from shorturl import views
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

# Route for the REST API
router = DefaultRouter()
router.register(r'shorturls', views.ShortcutUrlsViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
# include the REST API's routes
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls')),
# Redirection route
	url(r'^(?P<shortcut>\w{7})$', views.redirection),
# Route to obtain JWT Token
	url(r'^api/authenticate/$', obtain_jwt_token),
	url(r'^api/authenticate/renew/$', refresh_jwt_token),
# Web interface
	url(r'^$', views.base),
	url(r'^template/sign-form$', views.signFormTemplate, name='sign-form'),
	url(r'^template/index$', views.indexTemplate, name='index'),
	url(r'^template/shortcut/(?P<shortcut>\w{7})$', views.displayShortcutTemplate, name='display-shortcut')
]