from rest_framework import generics, status, viewsets, mixins, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework.decorators import action
from .permissions import IsSuperUser

from .models import User, Account, Transaction, Transfer
from .serializers import UserSerializer, AccountSerializer, TransactionSerializer, TransferSerializer

# =============================== API V1 ===============================

class UsersAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [IsAuthenticated]
  
class AccountsAPIView(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    # permission_classes = [IsAuthenticated]

class AccountAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    # permission_classes = [IsAuthenticated]
  
  
class TransactionsAPIView(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    # permission_classes = [IsAuthenticated]

class TransactionAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    # permission_classes = [IsAuthenticated]
  
  
class TransfersAPIView(generics.ListCreateAPIView):
    queryset = Transfer.objects.all()
    serializer_class = TransferSerializer
    # permission_classes = [IsAuthenticated]

class TransferAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transfer.objects.all()
    serializer_class = TransferSerializer
    # permission_classes = [IsAuthenticated]

    def get_object(self):
      if self.kwargs.get('user_pk'):
        return get_object_or_404(self.get_queryset(), user_pk=self.kwargs['user_pk'], pk=self.kwargs.get('transfer_pk'))
      return get_object_or_404(self.get_queryset(), pk=self.kwargs.get('transfer_pk'))

  
class MyAccountAPIView(APIView):
  # permission_classes = [IsAuthenticated]

  def get(self, request):
    account = Account.objects.filter(user=request.user).first()
    if not account:
      return Response({'detail': 'Conta não encontrada.'}, status=status.HTTP_404_NOT_FOUND)
    serializer = AccountSerializer(account)
    return Response(serializer.data)
  
# =============================== API V2 ===============================

class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer

  # Permissions
  # permission_classes = [permissions.DjangoModelPermissions]
  permission_classes = [IsSuperUser, permissions.DjangoModelPermissions]

  @action(detail=True, methods=['get'], permission_classes=[permissions.DjangoModelPermissions])
  def accounts(self, request, pk=None):
    user = self.get_object() # Get the user specified by pk # if all users will use self.queryset
    accounts = Account.objects.filter(user=user)
    serializer = AccountSerializer(accounts, many=True)
    return Response(serializer.data)

class AccountViewSet(viewsets.ModelViewSet):
  queryset = Account.objects.all()
  serializer_class = AccountSerializer
  permission_classes = [IsSuperUser, permissions.DjangoModelPermissions]

  @action(detail=True, methods=['get'], permission_classes=[IsSuperUser, permissions.DjangoModelPermissions])
  def transactions(self, request, pk=None):
    account = self.get_object() # Get the account specified by pk # if all accounts will use self.queryset

    self.pagination_class.page_size = 5
    transactions = Transaction.objects.filter(account=account)
    page = self.paginate_queryset(transactions)

    if page is not None:
        serializer = TransactionSerializer(page, many=True)
        return self.get_paginated_response(serializer.data)
    
    serializer = TransactionSerializer(transactions, many=True)
    return Response(serializer.data)

  @action(detail=True, methods=['get'], permission_classes=[permissions.DjangoModelPermissions])
  def transfers(self, request, pk=None):
    account = self.get_object() # Get the account specified by pk # if all accounts will use self.queryset
    transfers = Transfer.objects.filter(sender=account) | Transfer.objects.filter(receiver=account)
    transfers = transfers.distinct()
    serializer = TransferSerializer(transfers, many=True)
    return Response(serializer.data)