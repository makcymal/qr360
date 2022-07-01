from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import QRUser
from .forms import QRUserCreationForm, QRUserChangeForm


# class QRUserModelAdmin(admin.ModelAdmin):
#     prepopulated_fields = {'slug': ('id', )}


class QRUserAdmin(UserAdmin):
    
    add_form = QRUserCreationForm
    form = QRUserChangeForm
    model = QRUser

    list_display = (
        'username',
        'id',
        'is_staff',
        'is_active',
    )
    list_filter = (
        'is_staff',
        'is_active',
    )
    fieldsets = (
        (None, {
            'fields': (
                'username',
                'password',
            )
        }),
        ('Permissions', {
            'fields': (
                'is_staff',
                'is_active',
            )
        }),
    )
    add_fieldsets = ((None, {
        'classes': ('wide', ),
        'fields': (
            'username',
            'password1',
            'password2',
            'is_staff',
            'is_active',
        )
    }), )
    search_fields = ('username', )
    ordering = ('username', )


# admin.site.register(QRUser, QRUserModelAdmin)
admin.site.register(QRUser, QRUserAdmin)
