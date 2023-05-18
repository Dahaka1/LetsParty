from django.db import models
from events.models import Party
from main.models import User
from main.models import Creator
import main.business_logics


class UserPayment(models.Model):
	user = models.ForeignKey(
		User,
		on_delete=models.SET_NULL,
		null=True,
		verbose_name="Пользователь"
	)
	party = models.ForeignKey(
		Party,
		on_delete=models.SET_NULL,
		null=True,
		verbose_name="Вечеринка"
	)
	datetime = models.DateTimeField(
		auto_now_add=True,
		verbose_name="Дата и время"
	)
	amount = models.PositiveSmallIntegerField(
		null=True,
		verbose_name="Сумма"
	)
	
	def get_amount(self):  # when defining
		self.amount = main.business_logics.party_members_cost(self.party)
		
	class Meta:
		ordering = ["-datetime"]
		verbose_name = "Платежи пользователей"
		verbose_name_plural = verbose_name
		
	def __str__(self):
		return f'Платеж от {self.user}, {self.datetime}: {self.amount}'
		

class CreatorPayment(models.Model):
	creator = models.ForeignKey(
		Creator,
		on_delete=models.SET_NULL,
		null=True,
		verbose_name="Организатор"
	)
	party = models.ForeignKey(
		Party,
		on_delete=models.SET_NULL,
		null=True,
		verbose_name="Вечеринка"
	)
	datetime = models.DateTimeField(
		auto_now_add=True,
		verbose_name="Дата и время"
	)
	amount = models.SmallIntegerField(
		null=True,
		verbose_name="Сумма"
	)
	
	class Meta:
		ordering = ["-datetime"]
		verbose_name = "Платежи организаторов"
		verbose_name_plural = verbose_name
	
	def __str__(self):
		return f'Платеж от {self.creator}, {self.datetime}: {self.amount}'

	def get_amount(self):  # when defining
		self.amount = main.business_logics.party_creators_cost(self.party)
