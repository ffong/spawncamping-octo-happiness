from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.http import HttpRequest
from django.conf.urls.static import static
from django.conf import settings

from mysite import views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^$', views.index, name='index'),
	url(r'^polls/', include('polls.urls', namespace="polls")),
	url(r'^admin/', include(admin.site.urls)),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
