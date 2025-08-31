from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

# User model
class User(AbstractUser):
    cpf = models.CharField(max_length=11, unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.TextField(null=True, blank=True)
    groups = models.ManyToManyField(
        Group,
        related_name='banking_user_set',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='banking_user_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )

# Account bank model
class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="accounts")
    account_number = models.CharField(max_length=20, unique=True)
    agency = models.CharField(max_length=10, default="0001")
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)

    def deposit(self, amount):
        self.balance += amount
        self.save()

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.save()
            return True
        return False

# Register finance transactions (deposit, withdraw, transfer)
class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ("deposit", "Depósito"),
        ("withdraw", "Saque"),
        ("transfer", "Transferência"),
    ]

    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="transactions")
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(null=True, blank=True)

# Transfer model between accounts
class Transfer(models.Model):
    sender = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="sent_transfers")
    receiver = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="received_transfers")
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def process(self):
        if self.sender.withdraw(self.amount):
            self.receiver.deposit(self.amount)
            return True
        return False
