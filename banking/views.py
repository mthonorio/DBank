from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User, Account, Transaction, Transfer
from .serializers import UserSerializer, AccountSerializer, TransactionSerializer, TransferSerializer
from rest_framework.permissions import IsAuthenticated

class UsersAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
  
class AccountsAPIView(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [IsAuthenticated]

class AccountAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [IsAuthenticated]
  
  
class TransactionsAPIView(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]

class TransactionAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]
  
  
class TransfersAPIView(generics.ListCreateAPIView):
    queryset = Transfer.objects.all()
    serializer_class = TransferSerializer
    permission_classes = [IsAuthenticated]

class TransferAPIView(APIView):
  permission_classes = [IsAuthenticated]

  def get(self, request):
    user_accounts = Account.objects.filter(user=request.user)
    transfers = Transfer.objects.filter(
      sender__in=user_accounts
    ) | Transfer.objects.filter(
      receiver__in=user_accounts
    )
    transfers = transfers.distinct()
    serializer = TransferSerializer(transfers, many=True)
    return Response(serializer.data)
  
  def post(self, request):
    serializer = TransferSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  