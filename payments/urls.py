from django.urls import path
from . import views


urlpatterns = [
	path('<int:party_id>', views.party_payments)
]
