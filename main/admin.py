from django.contrib import admin
from main.models import *

models = [
	User,
	UserPreference,
	Creator,
	AgeGroup,
	District,
	SubCulture
]


class UserAdmin(admin.ModelAdmin):
	list_display = ("id", "nickname", "phone_number", "district", "last_callback")
	list_display_links = ("id", "nickname")
	search_fields = ("phone_number", "district")
	list_filter = ("last_callback", "tags")


class CreatorAdmin(admin.ModelAdmin):
	list_display = ("id", "user", "rating")
	list_display_links = ("id", "user")
	search_fields = ("id",)
	list_filter = ("rating", )


class SubCultureAdmin(admin.ModelAdmin):
	list_display = ("id", "title", "description")
	list_display_links = ("id", "title")
	search_fields = ("title", )


class DistrictAdmin(admin.ModelAdmin):
	list_display = ("id", "title", "city")
	list_display_links = ("id", "title")
	search_fields = ("title", "city")


class AgeGroupAdmin(admin.ModelAdmin):
	list_display = ("id", "title", "ages_range")
	list_display_links = ("id", "title")
	search_fields = ("title",)


class UserPreferenceAdmin(admin.ModelAdmin):
	list_display = ("user", "music_genre", "drink", "subculture")
	list_display_links = ("user", )
	search_fields = ("user", )
	list_filter = ("drink", "music_genre", "subculture")


admin.site.register(User, UserAdmin)
admin.site.register(UserPreference, UserPreferenceAdmin)
admin.site.register(Creator, CreatorAdmin)
admin.site.register(AgeGroup, AgeGroupAdmin)
admin.site.register(District, DistrictAdmin)
admin.site.register(SubCulture, SubCultureAdmin)
