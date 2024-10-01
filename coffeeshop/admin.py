from django.contrib import admin
from django.db import transaction as db_transaction  # Untuk memastikan atomicity
from .models.menu import Menu
from .models.transaction import Transaction, TransactionDetail
from .models.user import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'address')

    def save_model(self, request, obj, form, change):
        # Simpan User terlebih dahulu
        super().save_model(request, obj, form, change)

class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'category')

    def save_model(self, request, obj, form, change):
        # Simpan Menu terlebih dahulu
        super().save_model(request, obj, form, change)

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('user', 'total_amount')

    def save_model(self, request, obj, form, change):
        # Gunakan atomic block untuk memastikan semua data tersimpan dengan benar
        with db_transaction.atomic():
            # Simpan Transaction terlebih dahulu
            super().save_model(request, obj, form, change)

            # Setelah Transaction berhasil disimpan, buat TransactionDetail
            # Di sini, kita anggap bahwa satu transaksi memiliki satu detail transaksi.
            # Contoh: Otomatis menambahkan satu menu dengan quantity 1 untuk testing
            menu = Menu.objects.first()  # Ambil menu pertama sebagai contoh
            if menu:
                TransactionDetail.objects.create(
                    transaction=obj,
                    menu=menu,
                    quantity=1,  # Contoh kuantitas
                    subtotal=menu.price * 1  # Total harga = harga menu * kuantitas
                )

admin.site.register(User, UserAdmin)
admin.site.register(Menu, MenuAdmin)
admin.site.register(Transaction, TransactionAdmin)