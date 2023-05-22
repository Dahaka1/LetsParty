from __future__ import annotations

from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from taggit.managers import TaggableManager
import main.business_logics


class District(models.Model):
	title = models.CharField(
		max_length=50,
		verbose_name="Название"
	)
	city = models.CharField(
		max_length=50,
		default=None,
		null=True,
		verbose_name="Город"
	)

	class Meta:
		ordering = ["city"]
		verbose_name = "Районы"
		verbose_name_plural = verbose_name

	def __str__(self):
		return self.title


class SubCulture(models.Model):
	title = models.CharField(
		max_length=20,
		verbose_name="Название"
	)
	description = models.CharField(
		max_length=250,
		verbose_name="Описание"
	)

	class Meta:
		ordering = ["title"]
		verbose_name = "Субкультуры"
		verbose_name_plural = verbose_name

	def __str__(self):
		return f'"{self.title}"'


class AgeGroup(models.Model):
	groups = main.business_logics.config("AGE_GROUPS")
	title = models.CharField(
		choices=(
			(ttl, ttl) for ttl in groups.keys()
		),
		blank=False,
		unique=True,
		verbose_name="Название"
	)
	ages_range = models.CharField(
		max_length=5,
		choices=(
			(rng, rng) for rng in groups.values()
		),
		blank=False,
		unique=True,
		verbose_name="Границы"
	)

	def get_range(self):
		if self.ages_range:
			rng = map(int, self.ages_range.split('-'))
			return range(next(rng), next(rng) + 1)

	class Meta:
		ordering = ["ages_range"]
		verbose_name = "Возрастные группы"
		verbose_name_plural = verbose_name

	def __str__(self):
		return self.title

	def get_users(self) -> list[User]:
		return list(User.objects.filter(age_group=self))


class User(models.Model):
	nickname = models.CharField(
		max_length=50,
		verbose_name="Никнейм",
		null=True,
		default=None
	)
	district = models.ForeignKey(
		District,
		on_delete=models.PROTECT,
		null=True,
		default=None,
		verbose_name="Район"
	)
	phone_number = PhoneNumberField(
		null=False,
		unique=True,
		verbose_name="Номер телефона"
	)  # needs to get it by right way from form
	registration_date = models.DateTimeField(
		auto_now_add=True,
		verbose_name="Дата регистрации"
	)
	last_callback = models.DateTimeField(
		auto_now=True,
		null=True,
		verbose_name="Последняя активность"
	)
	gender = models.CharField(
		choices=main.business_logics.config("GENDERS"),
		default=None,
		verbose_name="Гендер"
	)
	age = models.PositiveSmallIntegerField(
		verbose_name="Возраст"
	)
	age_group = models.ForeignKey(
		AgeGroup,
		on_delete=models.PROTECT,
		default=None,
		verbose_name="Возрастная группа",
		null=True,
		blank=True
	)
	tags = TaggableManager(
		verbose_name="Теги",
		blank=True)

	subculture = models.ForeignKey(
		SubCulture,
		on_delete=models.PROTECT,
		verbose_name="Субкультура",
		default=None,
		null=True
	)

	class Meta:
		ordering = ["-registration_date"]
		verbose_name = "Пользователи"
		verbose_name_plural = verbose_name

	def get_absolute_url2(self):  # needs to define using django reverse
		pass

	def __str__(self):
		return self.nickname or "пусто"

	def get_age_group(self) -> None:
		groups = AgeGroup.objects.all()
		if groups:
			for group in groups:
				rng = group.get_range()
				if self.age in rng:
					if self.age_group is None or not self.age_group in rng:
						self.age_group = group
						self.save()

	def get_tags(self) -> list:
		return list(self.tags.all())

	def party_member_params(self) -> str:
		return f'{self.nickname}: {self.age_group}, субкультура: {self.subculture or "нет"}'


class Creator(models.Model):
	user = models.OneToOneField(
		User,
		on_delete=models.PROTECT,
		verbose_name="Пользователь"
	)
	rating = models.PositiveSmallIntegerField(
		help_text='val from 0 to 10',
		null=True,
		verbose_name="Рейтинг",
		blank=True
	)
	requisites_info = models.CharField(
		max_length=255,
		null=True,
		verbose_name="Реквизиты"
	)

	class Meta:
		ordering = ['user']
		verbose_name = "Организаторы"
		verbose_name_plural = verbose_name

	def get_absolute_url2(self):  # needs to define using django reverse
		pass

	def __str__(self):
		return f'{self.user.nickname}'


class UserPreference(models.Model):
	user = models.OneToOneField(
		User,
		on_delete=models.PROTECT,
		verbose_name="Пользователь",
		primary_key=True,
		unique=True
	)
	music_genre = models.CharField(
		choices=main.business_logics.config("MUSIC_GENRES"),
		blank=False,
		verbose_name="Жанр музыки"
	)
	drink = models.CharField(
		choices=main.business_logics.config("DRINKS_TYPES"),
		blank=False,
		verbose_name="Напиток"
	)

	class Meta:
		ordering = ["user"]
		verbose_name = "Предпочтения"
		verbose_name_plural = verbose_name
