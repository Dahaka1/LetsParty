from django.urls import path, re_path
from . import views


urlpatterns = [
	path("", views.show_all_events, name='events_page'),
	path("<slug:event_slug>/", views.show_event, name="event"),
	path("post", views.post_event, name='create_event')
]

