from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseAdmin
from django.contrib.auth.models import User

from users.models import Profile

class ProfileInline(admin.StackedInline):

	model = Profile
	verbose_name_plural = 'Profiles'
	can_delete = False
	
class UserAdmin(BaseAdmin):

	inlines = (ProfileInline,)
	#list_display = ('pk','username')
	
	
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

"""Registro de Profile en Admin como otro modulo
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

	list_display = ('pk','user', 'phone', 'web_site')
	list_display_links = ('pk', 'user')
	#list_editable = ('phone',)
	search_fields = ('user__username',)
	list_filter = ('user__date_joined', 'user__is_active','user__is_staff')
	
	fieldsets = (
		('Profile', {
				'fields': (
					('user', 'profile_picture'),
				)
			}
		),
		('More info', {
				'fields': (
					('phone', 'web_site'),
					('bio')
				)
			}
		),
		('Metadata', {
				'fields': (
					('date_modified',)
				)
			}
		)
	)
	
	readonly_fields = ('date_modified',)
"""