from django.urls import path, include
from . import views as auth_views

urlpatterns=[
	path('login_user/', (auth_views.login_user.as_view()), name='login_user'),
	path('register/', (auth_views.register.as_view()), name='register'),
	path('logout_user/', auth_views.logout_user , name='logout_user'),
	path('dashboard/', (auth_views.dashboard.as_view()), name='dashboard'),
	path('delete/', (auth_views.delete_account.as_view()), name='delete_account')
]