from django.contrib.auth.models import AnonymousUser

def restrict_staff(get_response):
	def mw(request):
		if request.user.is_staff and (not request.path.startswith('/admin/')):
			request.user=AnonymousUser()
		response=get_response(request)
		return response
	return mw