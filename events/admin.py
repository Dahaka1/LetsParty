from django.contrib import admin
from .models import *

models = [
	Party,
	PartyLocation
]


class PartyAdmin(admin.ModelAdmin):
	list_display = ("id", "creator", "date", "time", "members_amount", "budget", "is_closed")
	list_display_links = ("id", "date")
	search_fields = ("creator", "date", "time")
	list_filter = ("date", "time", "members_amount", "tags", "is_closed")


class PartyLocationAdmin(admin.ModelAdmin):
	list_display = ("party", "district", "address")
	list_display_links = ("party", )
	search_fields = list_display
	list_filter = ("district", )


admin.site.register(Party, PartyAdmin)
admin.site.register(PartyLocation, PartyLocationAdmin)