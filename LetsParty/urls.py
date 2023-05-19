from django.contrib import admin
from django.urls import re_path, path, include

from django.conf import settings
from django.conf.urls.static import static

from main.views import pageNotFound

urlpatterns = [
	re_path(r'^admin\/?', admin.site.urls),
	path("events/", include('events.urls')),
	path('', include('main.urls')),
	re_path(r'^pay\/?', include('payments.urls'))
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = pageNotFound
