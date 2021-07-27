from django.contrib import admin
from .models import User as custom_user
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin




class UserAdmin(BaseUserAdmin):
    list_display = ('email_or_phone', 'first_name')
    list_filter = ('first_name',)
    fieldsets = (
        (None, {'fields': ('email_or_phone', 'password')}),
        ('Personal info', {'fields': ('first_name','last_name')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email_or_phone', 'password'),
        }),
    )
    search_fields = ('email_or_phone',)
    ordering = ('email_or_phone',)
    filter_horizontal = ()


admin.site.register(custom_user, UserAdmin)