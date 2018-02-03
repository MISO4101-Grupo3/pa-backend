from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import ugettext_lazy as _

from .models import *
from .forms import PromoUserCreationForm, PromoUserChangeForm


# Register your models here.


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    """Define admin model for custom User model with no email field."""

    model = User
    add_form = PromoUserCreationForm
    form = PromoUserChangeForm

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Informacion Personal'), {'fields': ('first_name', 'last_name','foto','direccion','pais','favoritas')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)


admin.site.register(Categoria)
admin.site.register(Ciudad)
admin.site.register(Promocion)
admin.site.register(Comentario)
