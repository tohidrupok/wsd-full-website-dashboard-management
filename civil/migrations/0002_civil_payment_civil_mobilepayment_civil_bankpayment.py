# Generated by Django 5.0.2 on 2024-02-23 18:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('civil', '0001_initial'),
        ('civil_dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Civil_Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency', models.CharField(choices=[('USD', 'USD'), ('BDT', 'BDT')], max_length=3)),
                ('payment_amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('payment_type', models.CharField(choices=[('Online', 'Online'), ('Offline', 'Offline')], max_length=10)),
                ('payment_method', models.CharField(choices=[('bank', 'Bank'), ('mobile', 'Mobile')], max_length=10)),
                ('bank', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='civil_bank', to='civil_dashboard.civil_bank')),
                ('mobile_wallet', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='civil_mobile_wallet', to='civil_dashboard.civil_mobilewallet')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='civil_order_payment', to='civil.civil_order')),
            ],
        ),
        migrations.CreateModel(
            name='Civil_MobilePayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_holder_name', models.CharField(max_length=100)),
                ('account_holder_email', models.EmailField(max_length=254)),
                ('account_holder_phone', models.CharField(max_length=15)),
                ('mobile_wallet_name', models.CharField(max_length=100)),
                ('account_type', models.CharField(max_length=100)),
                ('account_info', models.TextField()),
                ('transaction_id', models.CharField(max_length=100, unique=True)),
                ('transaction_receipt', models.ImageField(upload_to='transaction_receipts/')),
                ('agree', models.BooleanField()),
                ('payment', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='mobile_payment', to='civil.civil_payment')),
            ],
        ),
        migrations.CreateModel(
            name='Civil_BankPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_holder_name', models.CharField(max_length=100)),
                ('account_holder_email', models.EmailField(max_length=254)),
                ('account_holder_phone', models.CharField(max_length=15)),
                ('bank_name', models.CharField(max_length=100)),
                ('account_number', models.CharField(max_length=50)),
                ('account_info', models.TextField(blank=True)),
                ('transaction_id', models.CharField(max_length=100, unique=True)),
                ('transaction_receipt', models.ImageField(upload_to='civil/image/transaction_receipts/')),
                ('additional_info', models.TextField(blank=True)),
                ('agree', models.BooleanField()),
                ('payment', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='bank_payment', to='civil.civil_payment')),
            ],
        ),
    ]
