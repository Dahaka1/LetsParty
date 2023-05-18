from django.urls import path, re_path
from . import views


urlpatterns = [
	path('', views.index, name='index_page'),
	re_path(r'^register\/?$', views.RegisterUser.as_view(), name='registering_page'),
	re_path(r'^about\/?$', views.about, name='about_page'),
	re_path(r'^login\/?$', views.login, name='logining_page')
]

