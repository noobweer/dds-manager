from django.contrib import admin
from django.http import JsonResponse

from .models import *
from rangefilter.filters import DateRangeQuickSelectListFilterBuilder
from django.urls import path

# Register your models here.
@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = (
        'created_date',
        'status',
        'type',
        'category',
        'subcategory',
        'amount',
        'short_comment',
    )
    list_filter = (
        ('created_date', DateRangeQuickSelectListFilterBuilder()),
        'status',
        'type',
        'category',
        'subcategory',
    )
    ordering = ['-created_date']
    list_per_page = 25

    # Shorted version of comment (Full comment if len < 10 else 10 symbols + ...)
    def short_comment(self, obj):
        return obj.comment[:10] + '...' if obj.comment and len(obj.comment) > 10 else obj.comment

    short_comment.short_description = 'Комментарий'

    # Functions for auto updating inputs/dropdown menus for categories and subcategories
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('filter-categories/', self.admin_site.admin_view(self.filter_categories), name='filter-categories'),
            path('filter-subcategories/', self.admin_site.admin_view(self.filter_subcategories),
                 name='filter-subcategories'),
        ]
        return custom_urls + urls

    def filter_categories(self, request):
        type_id = request.GET.get('type_id')
        categories = Category.objects.filter(type_id=type_id).values('id', 'name')
        return JsonResponse(list(categories), safe=False)

    def filter_subcategories(self, request):
        category_id = request.GET.get('category_id')
        subcategories = Subcategory.objects.filter(category_id=category_id).values('id', 'name')
        return JsonResponse(list(subcategories), safe=False)

    class Media:
        js = ('admin/js/transaction_admin.js',)


admin.site.register(OperationType)
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Status)
