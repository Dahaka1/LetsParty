from django.shortcuts import render
from events.models import Party
from django.http import Http404


def party_payments(request, party_id):
	try:
		party = next(iter(Party.objects.filter(pk=party_id)))
		#
	except StopIteration:
		raise Http404

