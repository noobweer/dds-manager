from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = (
        'custom_date',
        'status',
        'type',
        'category',
        'subcategory',
        'amount',
        'short_comment',
    )
    list_filter = (
        'custom_date',
        'status',
        'type',
        'category',
        'subcategory',
    )
    ordering = ['-custom_date']
    list_per_page = 25

    def short_comment(self, obj):
        return obj.comment[:10] + '...' if obj.comment and len(obj.comment) > 30 else obj.comment
    short_comment.short_description = 'Комментарий'


admin.site.register(OperationType)
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Status)
