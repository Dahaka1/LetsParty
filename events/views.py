from django.shortcuts import render
from django.views.generic import ListView
from .models import Party
import main.business_logics
from django.http import HttpResponse
import main.business_logics


def show_all_events(request):
	page_title = main.business_logics.config("EVENTS_PAGE")
	return render(request, 'events/events.html', page_title)


def show_event(request, event_id):
	params = main.business_logics.party_details_params(event_id)
	return render(request, 'events/event_details.html', params)
