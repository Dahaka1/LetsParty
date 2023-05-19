from __future__ import annotations
from django import template
from events.models import *
from typing import Optional
from django.http import Http404


register = template.Library()


@register.inclusion_tag('events/tags_templates/event.html')
def show_event(event_id: int) -> dict[str, Party]:
	try:
		event = next(iter(Party.objects.filter(pk=event_id)))
		return {"EVENT": event}
	except StopIteration:
		raise Http404


@register.simple_tag()
def get_all_events() -> QuerySet[Party]:
	out = Party.all()
	return out


@register.simple_tag()
def get_upcoming_events() -> Optional[list[Party]]:
	events = get_all_events()
	out = list(filter(lambda event: event.datetime() - datetime.now() > timedelta(hours=3), events))
	if any(out):
		return out


@register.simple_tag()
def get_nearest_events() -> Optional[list[Party]]:
	events = get_upcoming_events()
	out = list(filter(lambda event: event.datetime() - datetime.now() <= timedelta(days=5), events))
	if any(out):
		return out


@register.simple_tag()
def get_event_by_id(event_id) -> Optional[Party]:
	if not event_id is None:
		party = get_all_events().filter(pk=event_id)
		try:
			return next(iter(party))
		except StopIteration:
			raise Http404


@register.inclusion_tag('events/tags_templates/event_details.html')
def show_event_details(event_id):
	event = get_event_by_id(event_id)
	return {"EVENT": event}


@register.inclusion_tag('events/tags_templates/list_events.html')
def show_events(list_type: str, event_id=None) -> dict[str, list[Party] | QuerySet[Party]]:
	list_types = {
		"ALL": get_all_events,
		"UPCOMING": get_upcoming_events,
		"NEAREST": get_nearest_events,
		"SPECIFIC": get_event_by_id(event_id)
	}
	events = list_types[list_type]() if not list_type == "SPECIFIC" else list_types[list_type]
	if list_type == "NEAREST":
		events = events[:3]
	return {"EVENTS_LIST": events,
			"OUTPUT_TYPE": list_type,
			"EVENTS_LIST_LENGTH": len(events) if not list_type == "SPECIFIC" else 1}