from django.conf.urls import include, url
from django.contrib import admin
from oauth2_provider import urls as oauth_urls
from cms.member import urls as member_api
import api
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^oauth/', include(oauth_urls, namespace='oauth2_provider')),

    url(r'^api/', include(api)),

]
