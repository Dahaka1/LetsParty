from django.urls import path, re_path
from . import views


urlpatterns = [
	path("", views.show_all_events, name='events_page'),
	path("<int:event_id>/", views.show_event, name="event")
]

