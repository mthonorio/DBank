from rest_framework import serializers
from .models import User, Account, Transaction, Transfer

class UserSerializer(serializers.ModelSerializer):
    accounts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'cpf', 'date_of_birth', 'phone_number', 'address', 'is_staff', 'is_active', 'accounts']

class AccountSerializer(serializers.ModelSerializer):
    transactions = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Account
        fields = ['id', 'user', 'account_number', 'agency', 'balance', 'created_at', 'transactions']
        read_only_fields = ['balance', 'created_at']

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'account', 'transaction_type', 'amount', 'created_at', 'description']
        read_only_fields = ['created_at']

class TransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transfer
        fields = ['id', 'sender', 'receiver', 'amount', 'created_at']
        read_only_fields = ['created_at']
