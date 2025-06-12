from django.urls import path
from .views import *

urlpatterns = [
    # All urls for transactions
    path('create-transaction/', CreateTransactionView.as_view(), name='create-transaction'),
    path('delete-transaction/', DeleteTransactionView.as_view(), name='delete-transaction'),
    path('edit-transaction/', EditTransactionView.as_view(), name='edit-transaction'),
    path('transactions/', TransactionsView.as_view(), name='transactions'),

    # All urls for statuses
    path('create-status/', CreateStatusView.as_view(), name='create-status'),
    path('delete-status/', DeleteStatusView.as_view(), name='delete-status'),
    path('edit-status/', EditStatusView.as_view(), name='edit-status'),
    path('statuses/', StatusesView.as_view(), name='statuses'),

    # All urls for types
    path('create-type/', CreateTypeView.as_view(), name='create-type'),
    path('delete-type/', DeleteTypeView.as_view(), name='delete-type'),
    path('edit-type/', EditTypeView.as_view(), name='edit-type'),
    path('types/', TypesView.as_view(), name='types'),

    # All urls for categories
    path('create-category/', CreateCategoryView.as_view(), name='create-category'),
    path('delete-category/', DeleteCategoryView.as_view(), name='delete-category'),
    path('edit-category/', EditCategoryView.as_view(), name='edit-category'),
    path('categories/', CategoriesView.as_view(), name='categories'),

    # All urls for subcategories
    path('create-subcategory/', CreateSubcategoryView.as_view(), name='create-subcategory'),
    path('delete-subcategory/', DeleteSubcategoryView.as_view(), name='delete-subcategory'),
    path('edit-subcategory/', EditSubcategoryView.as_view(), name='edit-subcategory'),
    path('subcategories/', SubcategoriesView.as_view(), name='subcategories')
]
