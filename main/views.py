from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
import main.business_logics


def index(request):
	page_title = main.business_logics.config("INDEX_PAGE")
	return render(request, 'main/index.html', page_title)


def about(request):
	title = main.business_logics.config("ABOUT_PAGE")
	return render(request, 'main/about.html', title)


def login(request):
	title = main.business_logics.config("LOGIN_PAGE")
	return render(request, 'main/login.html', title)


def pageNotFound(request, exception):
	return redirect('index_page', permanent=True)


class RegisterUser(CreateView):
	form_class = UserCreationForm
	template_name = 'main/register.html'
	success_url = reverse_lazy('logining_page')

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super().get_context_data(**kwargs)
		c_def = self.get_user_context(title="Регистрация")
		return dict(list(context.items() + list(c_def.items())))
