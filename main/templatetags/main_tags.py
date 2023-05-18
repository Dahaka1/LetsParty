from __future__ import annotations

from django import template
from django.db.models import QuerySet
from events.models import *
from datetime import datetime, timedelta
import main.business_logics
from typing import Optional

register = template.Library()


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
def main_menu() -> list[dict[str, str]]:
	return main.business_logics.config("MAIN_MENU")


@register.inclusion_tag('main/tags_templates/list_events.html')
def show_events(list_type: str) -> dict[str, list[Party] | QuerySet[Party]]:
	list_types = {
		"ALL": get_all_events,
		"UPCOMING": get_upcoming_events,
		"NEAREST": get_nearest_events
	}
	events = list_types[list_type]()
	return {"EVENTS_LIST": events}
