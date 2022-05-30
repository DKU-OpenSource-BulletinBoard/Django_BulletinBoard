from django.contrib import admin
from .models import User

@admin.register(User)
class UserManage(admin.ModelAdmin):
    list_of_user = (
        'u_id',
        'u_pw',
        'u_name',
        'u_phone',
        'u_register_date'
    )

# Register your models here.
