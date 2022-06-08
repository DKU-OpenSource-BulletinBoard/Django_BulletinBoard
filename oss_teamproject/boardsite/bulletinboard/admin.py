from django.contrib import admin
from .models import BulletinBoard
from django_summernote.admin import SummernoteModelAdmin

@admin.register(BulletinBoard)
class BoardAdmin(SummernoteModelAdmin):
    summernote_fields = ('contents',)
    list_display = (
        'title',
        'contents',
        'username',
        'board_category',
        'write_date',
        'last_update',
        'view_count'
    )
    list_display_links = list_display

# Register your models here.
