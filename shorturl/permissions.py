from rest_framework import permissions

class IsOwner(permissions.BasePermission):
	"""
	Custom permission to allow owner to see statistics of his shortcuts
	"""
	def has_object_permission(self, request, view, obj):
		return obj.owner == request.user