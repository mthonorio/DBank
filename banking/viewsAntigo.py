from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User, Account, Transaction, Transfer
from .serializers import UserSerializer, AccountSerializer, TransactionSerializer, TransferSerializer
from rest_framework.permissions import IsAuthenticated

class UserAPIView(APIView):
  def get(self, request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)
  
  def post(self, request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
class AccountAPIView(APIView):
  permission_classes = [IsAuthenticated]

  def get(self, request):
    accounts = Account.objects.all()
    serializer = AccountSerializer(accounts, many=True)
    return Response(serializer.data)
  
  def post(self, request):
    serializer = AccountSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
class TransactionAPIView(APIView):
  permission_classes = [IsAuthenticated]

  def get(self, request):
    transactions = Transaction.objects.all()
    serializer = TransactionSerializer(transactions, many=True)
    return Response(serializer.data)
  
  def post(self, request):
    serializer = TransactionSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
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