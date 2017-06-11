from rest_framework import permissions

class IsOwner(permissions.BasePermission):
	"""
	Custom permission to allow owner to see statistics of his shortcuts
	"""
	def has_object_permission(self, request, view, obj):
		return obj.owner == request.user or request.user.is_staff


class UserPermission(permissions.BasePermission):
	"""
	Custom permission
		Allow anybody to create user
		Owner to modify their account
		Admin to do everything
	"""
	def has_permission(self, request, view):
		if view.action == 'list':
			return request.user.is_staff
		else:
			return True

	def has_object_permission(self, request, view, obj):
		return request.user.is_staff or obj == request.user