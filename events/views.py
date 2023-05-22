from django.shortcuts import render, get_object_or_404, redirect
import main.business_logics
import main.business_logics
from events.forms import AddEventForm
from events.models import *


def show_all_events(request):
	page_title = main.business_logics.config("EVENTS_PAGE")
	return render(request, 'events/events.html', page_title)


def show_event(request, event_slug):
	event = get_object_or_404(Party, slug=event_slug)
	params = main.business_logics.party_details_params(event.id)
	params['event'] = event
	return render(request, 'events/event_details.html', params)


def post_event(request):
	params = main.business_logics.config("EVENT_POST_PAGE")
	if request.method == "POST":
		form = AddEventForm(request.POST)
		if form.is_valid():
			# it needs to add user checking
			try:
				if event_date_checking:
					form.instance.define_params()
					form.save()
					return redirect('events_page')
				else:
					form.add_error("time", 'Уже есть мероприятие в это время!')
			except Exception as e:
				print(e)
				form.add_error(None, 'Ошибка создания формы')
	elif request.method == "GET":
		form = AddEventForm()

	params["FORM"] = form
	return render(request, 'events/event_post.html', params)
