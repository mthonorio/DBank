from django.urls import path
from .views import UsersAPIView, AccountsAPIView, TransactionsAPIView, TransfersAPIView, UserAPIView, AccountAPIView, TransactionAPIView, TransferAPIView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('users/', UsersAPIView.as_view(), name='users'),
    path('user/<int:pk>', UserAPIView.as_view(), name='user'),
    path('accounts/', AccountsAPIView.as_view(), name='accounts'),
    path('account/<int:pk>', AccountAPIView.as_view(), name='account'),
    path('transactions/', TransactionsAPIView.as_view(), name='transactions'),
    path('transaction/<int:pk>', TransactionAPIView.as_view(), name='transaction'),
    path('transfers/', TransfersAPIView.as_view(), name='transfers'),
    path('transfer/<int:pk>', TransferAPIView.as_view(), name='transfer'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]