
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model



class CustomUserAdmin(UserAdmin):
    """Define admin model for custom User model with no username field."""
    fieldsets = (
        (None, {'fields': ('email','phone', 'password')}),
        (_('Personal info'), {'fields': ('username', 'dob')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email','phone', 'password1', 'password2'),
        }),
    )
    list_display = ('email','phone', 'username', 'first_name',)
    search_fields = ('email','phone' 'first_name', 'last_name')
    ordering = ('email','phone')


admin.site.register(get_user_model(), CustomUserAdmin)






# Register your models here.


# Register your models here.
