from django.conf.urls import url, include
from shorturl import views
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from rest_framework.documentation import include_docs_urls

# Route for the REST API
router = DefaultRouter()
router.register(r'shorturls', views.ShortcutUrlsViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
# include the REST API's routes
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^docs/', include_docs_urls(title='BitLy Like API')),
# Redirection route
	url(r'^(?P<shortcut>\w{7})$', views.redirection),
# Route to obtain JWT Token
	url(r'^api/authenticate/$', obtain_jwt_token, name='obtain-token'),
	url(r'^api/authenticate/renew/$', refresh_jwt_token, name='renew-token'),
# Web interface
	url(r'^$', views.base),
	url(r'^template/sign-form$', views.signFormTemplate, name='sign-form'),
	url(r'^template/index$', views.indexTemplate, name='index'),
	url(r'^template/shortcut$', views.displayShortcutTemplate, name='display-shortcut'),
	url(r'^template/indexLogin$', views.indexLoginTemplate, name='index-login'),
	url(r'^template/statistics$', views.statisticsTemplate, name='statistics'),
]