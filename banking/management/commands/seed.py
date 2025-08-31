from django.core.management.base import BaseCommand
from banking.models import User, Account, Transaction, Transfer
from django.utils import timezone

class Command(BaseCommand):
	help = 'Popula o banco de dados com dados de exemplo.'

	def handle(self, *args, **kwargs):
		# Usuários
		user1, _ = User.objects.get_or_create(username='alice', defaults={
			'cpf': '12345678901',
			'date_of_birth': '1990-01-01',
			'phone_number': '11999999999',
			'address': 'Rua A, 123',
		})
		user1.set_password('senha123')
		user1.save()

		user2, _ = User.objects.get_or_create(username='bob', defaults={
			'cpf': '98765432100',
			'date_of_birth': '1985-05-05',
			'phone_number': '21988888888',
			'address': 'Rua B, 456',
		})
		user2.set_password('senha123')
		user2.save()

		# Contas
		acc1, _ = Account.objects.get_or_create(user=user1, account_number='00001')
		acc2, _ = Account.objects.get_or_create(user=user2, account_number='00002')

		# Transações
		Transaction.objects.get_or_create(account=acc1, transaction_type='deposit', amount=1000, description='Depósito inicial')
		Transaction.objects.get_or_create(account=acc2, transaction_type='deposit', amount=500, description='Depósito inicial')

		# Transferência
		Transfer.objects.get_or_create(sender=acc1, receiver=acc2, amount=200)

		self.stdout.write(self.style.SUCCESS('Banco de dados populado com sucesso!'))
