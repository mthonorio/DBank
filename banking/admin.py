from django.contrib import admin
from .models import User, Account, Transaction, Transfer

# admin.site.register(User)
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'cpf', 'date_of_birth', 'phone_number', 'address', 'is_staff', 'is_active')
    search_fields = ('username', 'email', 'cpf')
    list_filter = ('is_staff', 'is_active')

    
    fieldsets = (
        (None, {'fields': ('username', 'email', 'cpf', 'date_of_birth', 'phone_number', 'address')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('account_number', 'user', 'agency', 'balance', 'created_at')
    search_fields = ('account_number', 'user__username', 'user__email')
    list_filter = ('agency', 'created_at')
    
    fieldsets = (
        (None, {'fields': ('user', 'account_number', 'agency', 'balance')}),
        ('Timestamps', {'fields': ('created_at',)}),
    )
    readonly_fields = ('created_at',)
@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('account', 'transaction_type', 'amount', 'created_at', 'description')
    search_fields = ('account__account_number', 'account__user__username', 'transaction_type')
    list_filter = ('transaction_type', 'created_at')
    
    fieldsets = (
        (None, {'fields': ('account', 'transaction_type', 'amount', 'description')}),
        ('Timestamps', {'fields': ('created_at',)}),
    )
    readonly_fields = ('created_at',)
