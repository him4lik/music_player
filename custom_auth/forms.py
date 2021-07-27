from django import forms
from .models import User as user_model
from django.core.exceptions import ValidationError
import re
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth import authenticate

class login_form(forms.Form):
	email_or_phone=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Or Phone...'}))
	password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder': 'Password...'}))

	
	
	def clean(self):
		cleaned_data = super().clean()
		e_or_p = cleaned_data.get("email_or_phone")
		password = cleaned_data.get("password")
		try:
			value=int(e_or_p)
		except:
			regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
			if not (re.match(regex, e_or_p)):
				raise forms.ValidationError('Invalid email')
		else:
			if len(str(e_or_p))!=12:
				raise forms.ValidationError('12 digits')

		user=authenticate(email_or_phone=e_or_p, password=password)
		if user==None:
			raise forms.ValidationError("User doesn't exist")
		if user.is_staff:
			raise  forms.ValidationError("Staff users don't have access")
	

		
class register_form(forms.ModelForm):
	
	class Meta:
		model=user_model
		fields=['first_name','last_name', 'email_or_phone', 'password']
		widgets={'password': forms.PasswordInput(attrs={'class':'form-control', 'placeholder': 'Password...'}),
				 'email_or_phone': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Or Phone...'}),
				 'first_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'First name...'}),
				 'last_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name...'}),
				 
				}


	def save(self):
		user=super().save(commit=False)
		user.set_password(self.cleaned_data["password"])
		user.save()
		return user

class user_info_form(forms.ModelForm):
	class Meta:
		model=user_model
		fields=['first_name', 'last_name', 'email_or_phone']


class change_password_form(forms.Form):
	current_password=forms.CharField(widget=forms.PasswordInput)
	new_password=forms.CharField(widget=forms.PasswordInput)
	retype_password=forms.CharField(widget=forms.PasswordInput)
	email_or_phone=forms.CharField(widget=forms.HiddenInput)

	def clean(self):
		cleaned_data = super().clean()
		current_password=cleaned_data.get('current_password')
		new_password = cleaned_data.get("new_password")
		retype_password = cleaned_data.get("retype_password")
		email_or_phone=cleaned_data.get("email_or_phone")
		if new_password!=retype_password:
			raise forms.ValidationError("New password didn't match")
		user=authenticate(email_or_phone=email_or_phone, password=current_password)
		if user==None:
			raise forms.ValidationError('Incorrect current password')

class delete_account_form(forms.Form):
	password=forms.CharField(widget=forms.PasswordInput)
	email_or_phone=forms.CharField(widget=forms.HiddenInput)

	def clean(self):
		cleaned_data=super().clean()
		password=cleaned_data.get('password')
		email_or_phone=cleaned_data.get('email_or_phone')
		user=authenticate(email_or_phone=email_or_phone, password=password)
		if user==None:
			raise forms.ValidationError('Incorrect password')


class UserCreationForm(forms.ModelForm):
    
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    

    class Meta:
        model = user_model
        fields = ('email_or_phone', )

    

    def save(self, commit=True):
       
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = user_model
        fields = ('email_or_phone', 'password', 'is_active',)