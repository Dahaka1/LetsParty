from django.views.generic import ListView
from .models import Party
import main.business_logics


class EventsHome(ListView):
	model = Party
	template_name = "main/base.html"
	context_object_name = 'events'

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super().get_context_data(**kwargs)
		context["MENU"] = main.business_logics.config("MAIN_MENU")
		params = main.business_logics.config("EVENTS_PAGE")
		for param in params:
			context[param] = params[param]
		return context
