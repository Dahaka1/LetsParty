from django.db import models
from django.db.models import QuerySet
from main.models import Creator, AgeGroup, SubCulture, District, User
from taggit.managers import TaggableManager
import main.business_logics
from datetime import date, timedelta, datetime


class PartyLocation(models.Model):
	district = models.ForeignKey(
		District,
		on_delete=models.PROTECT,
		verbose_name="Район"
	)
	party = models.OneToOneField(
		"Party",
		on_delete=models.PROTECT,
		primary_key=True,
		unique=True,
		verbose_name="Вечеринка"
	)
	address = models.CharField(
		max_length=255,
		verbose_name="Адрес"
	)

	class Meta:
		ordering = ["district"]
		verbose_name = "Локации"
		verbose_name_plural = verbose_name

	def __str__(self):
		return f'{self.district}, {self.address}'


class Party(models.Model):  # paid events only
	default_params = main.business_logics.config("PARTY")
	default_date = date.today() + timedelta(days=default_params["DEFAULT_IN_DAYS"])
	default_time = default_params["DEFAULT_TIME"]

	creator = models.ForeignKey(
		Creator,
		on_delete=models.PROTECT,
		verbose_name="Организатор"
	)
	members_amount = models.PositiveSmallIntegerField(
		verbose_name="Максимальное количество участников"
	)
	date = models.DateField(
		default=default_date,
		verbose_name="Дата"
	)
	time = models.TimeField(
		default=default_time,
		verbose_name="Время"
	)
	tags = TaggableManager(
		verbose_name="Теги"
	)
	age_group = models.ForeignKey(
		AgeGroup,
		on_delete=models.PROTECT,
		blank=True,
		null=True,
		default=None,
		verbose_name="Возрастная группа"
	)
	preferred_gender = models.CharField(
		choices=main.business_logics.config("GENDERS"),
		null=True,
		verbose_name="Предпочтительный гендер",
		default=None,
		blank=True
	)
	subculture = models.ForeignKey(
		SubCulture,
		on_delete=models.PROTECT,
		blank=False,
		verbose_name="Субкультура",
		null=True,
		default=None
	)
	music_genre = models.CharField(
		choices=main.business_logics.config("MUSIC_GENRES"),
		blank=False,
		null=True,
		default=None,
		verbose_name="Жанр музыки"
	)
	budget = models.PositiveIntegerField(
		default=0,
		verbose_name="Бюджет"
	)
	users = models.ManyToManyField(
		User
	)  # users who did pay for party
	is_closed = models.BooleanField(
		default=False,
		verbose_name="Набор закрыт"
	)

	class Meta:
		ordering = ["-date", "-time"]
		db_table = "events_parties"
		verbose_name = "Мероприятия"
		verbose_name_plural = verbose_name

	def get_absolute_url2(self):  # needs to define for using django reverse
		pass

	def __str__(self):
		return f'ID: {self.id}, {self.date}, {str(self.time)[:-3]} (организатор: {self.creator.user.nickname})'

	def define_age_group(self):  # when creating
		if self.age_group is None:
			self.age_group = self.creator.user.age_group
			self.save()

	def get_location(self):
		try:
			return next(iter(PartyLocation.objects.filter(pk=self)))
		except StopIteration:
			pass

	@staticmethod
	def all() -> QuerySet:
		return Party.objects.all().order_by('-date', '-time', 'creator', 'members_amount')

	def datetime(self) -> datetime:
		dt = datetime.combine(self.date, self.time)
		return dt

