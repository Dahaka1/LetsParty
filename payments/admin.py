from django.contrib import admin
from .models import CreatorPayment, UserPayment


class UserPaymentAdmin(admin.ModelAdmin):
	list_display = ("id", "user", "party", "amount", "datetime")
	list_filter = ("amount", "datetime")
	list_display_links = ("id", "datetime")
	search_fields = ("user", "party", "datetime")


class CreatorPaymentAdmin(admin.ModelAdmin):
	list_display = ("id", "creator", "party", "amount", "datetime")
	list_filter = ("amount", "datetime")
	list_display_links = ("id", "datetime")
	search_fields = ("creator", "party", "datetime")


admin.site.register(UserPayment, UserPaymentAdmin)
admin.site.register(CreatorPayment, CreatorPaymentAdmin)
