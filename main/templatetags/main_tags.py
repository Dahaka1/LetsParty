from django import template
import main.business_logics


register = template.Library()


@register.simple_tag()
def main_menu() -> list[dict[str, str]]:
	return main.business_logics.config("MAIN_MENU")


@register.simple_tag()
def sub_menu() -> list[dict[str, str]]:
	return main.business_logics.config("SUB_MENU")