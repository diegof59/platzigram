"""Platzigram Users middleware catalog."""

from django.shortcuts import redirect
from django.urls import reverse


class ProfileCompletionMiddleware:
	"""Profile completion middleware.
	Restringe el uso de la app de tal manera que un usuario deba tener Bio y Profile pic.
	"""
	def __init__(self, get_response):
	
		self.get_response = get_response

	def __call__(self, request):
		"""Codigo ejecutado cada request, antes de la llamada al view."""
		if not request.user.is_anonymous:
			if not request.user.is_staff:
				profile = request.user.profile
				if not profile.profile_picture or not profile.bio:
					if request.path not in [reverse('update'), reverse('logout')]:
						return redirect('update')
						
		response = self.get_response(request)
		return response
