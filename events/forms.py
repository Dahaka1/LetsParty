from django import forms
from django.core.exceptions import ValidationError
from datetime import date, timedelta, datetime
from .models import *
import main.business_logics


class AddEventForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		for field in ["creator", "subculture"]:
			self.fields[field].empty_label = "не выбрано"

	class Meta:
		model = Party
		fields = [
			'creator', 'members_amount', 'date', 'time',
			'preferred_gender', 'subculture', 'music_genre', 'budget'
		]

	# validation method
	def clean_budget(self):
		budget = self.cleaned_data["budget"]
		max_value = main.business_logics.config("MAX_BUDGET")
		if budget > max_value:
			raise ValidationError("Бюджет не может быть больше 20000 рублей.")

		return budget

	def clean_members_amount(self):
		members_amount = self.cleaned_data["members_amount"]
		max_value = main.business_logics.config("MAX_MEMBERS_AMOUNT")
		if members_amount > max_value:
			raise ValidationError(f"Участников вечеринки не может быть больше {max_value}!")

		return members_amount

	def clean_date(self):
		event_date = self.cleaned_data["date"]
		max_planning_period = main.business_logics.config("MAX_PLANNING_PERIOD")
		if event_date < date.today():
			raise ValidationError("Дата не может быть в прошлом!")
		elif event_date - date.today() > timedelta(days=max_planning_period):
			raise ValidationError(f"Запланировать мероприятие можно на срок максимум в течение {max_planning_period} дней!")
		elif event_date == date.today():
			raise ValidationError(f"Запланировать мероприятие можно минимум на завтрашний день!")
		return event_date

