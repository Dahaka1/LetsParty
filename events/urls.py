from django.urls import path, re_path, include
from . import views


urlpatterns = [
	path("", views.EventsHome.as_view(), name='events_page')
]

