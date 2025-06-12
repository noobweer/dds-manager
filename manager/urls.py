from django.urls import path
from .views import *

urlpatterns = [
    path('create-transaction/', CreateTransactionsView.as_view(), name='create-transaction'),
    path('delete-transaction/', DeleteTransactionView.as_view(), name='delete-transaction'),
    path('')
]
