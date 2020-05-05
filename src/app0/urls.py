from django.conf.urls.i18n import i18n_patterns
from django.urls import include, path
from django.contrib import admin

from . import views

urlpatterns = i18n_patterns(
	path( "i18n/", include( "django.conf.urls.i18n" ) )
	, path( "index/", views.index )
	, path( "admin/", admin.site.urls )
	, path( "", include( "cms.urls" ) )
	, prefix_default_language = False
)
