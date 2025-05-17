from django.urls import path
from tracker.views import index, deleteTransaction

urlpatterns = [
    path('', index, name='index'),
    path('delete-transaction/<uuid>/', deleteTransaction, name='deleteTransaction'),
]