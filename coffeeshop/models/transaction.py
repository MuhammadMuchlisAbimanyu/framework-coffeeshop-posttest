from django.db import models
from .user import User
from .menu import Menu
from django.core.validators import MinValueValidator

class Transaction(models.Model):
    # transaction_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, validators=[
        MinValueValidator(0)  # Jumlah total tidak boleh negatif
    ])
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Transaction {self.id} by {self.user.name}'

class TransactionDetail(models.Model):
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    quantity = models.IntegerField(validators=[
        MinValueValidator(1)  # Kuantitas minimal adalah 1
    ])
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.quantity} x {self.menu.name}'
