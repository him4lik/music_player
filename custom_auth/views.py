from django.shortcuts import render, redirect
from django import views
from .forms import login_form, register_form, user_info_form, change_password_form, delete_account_form
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


class login_user(views.View):
	template_name='custom_auth/login-page.html'
	form=login_form
	redirect_url='home'

	
	def get(self, request):
		if request.user.is_authenticated:
			return redirect('home')
		fm=self.form()
		context={'form':fm}
		return render(request, self.template_name, context)

	
	def post(self, request):
		fm=self.form(request.POST)
		context={'form': fm}
		if fm.is_valid():
			user=authenticate(request, email_or_phone=fm.cleaned_data['email_or_phone'], password=fm.cleaned_data['password'])
			login(request, user)
			if len(request.GET)!=0:
				self.redirect_url=request.GET.get('next')
			return redirect(self.redirect_url)
		else:
			return render(request, self.template_name, context)


class register(views.View):
	template_name='custom_auth/register.html'
	form=register_form
	redirect_url='login_user'

	def get(self, request):
		if request.user.is_authenticated:
			logout()
			return redirect('register')
		fm=self.form
		context={'form':fm}
		return render(request, self.template_name, context)

	def post(self, request):
		fm=self.form(request.POST)
		context={'form':fm}
		print(request.POST)
		if fm.is_valid():
			fm.save()
			return redirect(self.redirect_url)
		else:
			return render(request, self.template_name, context)


class dashboard(LoginRequiredMixin, views.View):
	login_url='login_user'
	form1=user_info_form
	form2=change_password_form
	redirect_url='dashboard'
	template_name='custom_auth/dashboard.html'
	def get(self, request):
		fm1=self.form1(instance=request.user)
		fm2=self.form2(initial={'email_or_phone':request.user.email_or_phone})
		context={'form1':fm1, 'form2':fm2, }
		return render(request, self.template_name, context)

	def post(self, request):
		if request.POST.get('first_name'):
			fm1=self.form1(request.POST, instance=request.user)
			fm2=self.form2()
			if fm1.is_valid():
				fm1.save()
			return redirect('dashboard')
		else:
			fm2=self.form2(request.POST)
			fm1=self.form1(instance=request.user)
			if fm2.is_valid():
				new_password=fm2.cleaned_data['new_password']
				user=request.user
				user.set_password(new_password)
				user.save()
				logout(request)
				return redirect('login_user')
			context={'form1':fm1, 'form2':fm2, }

			return render(request, 'custom_auth/dashboard.html', context)



class delete_account(LoginRequiredMixin , views.View):
	login_url='login_user'
	template_name='custom_auth/delete_account.html'
	form=delete_account_form
	redirect_url='login_user'

	def get(self, request):
		fm=self.form(initial={'email_or_phone':request.user.email_or_phone})
		context={'form':fm}
		return render(request, self.template_name, context)

	def post(self, request):
		fm=self.form(request.POST)
		context={'form':fm}
		if fm.is_valid():
			user=request.user
			user.delete()
			return redirect(self.redirect_url)
		else:
			return render(request, self.template_name, context)


@login_required(login_url='login_user')
def logout_user(request):
	logout(request)
	return redirect('home')

