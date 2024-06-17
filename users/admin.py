from django.contrib import admin
from .models import User
# Register your models here.

from django.contrib import admin

from products.admin import BasketAdmin
from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username',)
    inlines = (BasketAdmin,)
