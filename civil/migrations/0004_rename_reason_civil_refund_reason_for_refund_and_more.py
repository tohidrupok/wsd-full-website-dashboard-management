# Generated by Django 5.0.2 on 2024-02-26 08:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('civil', '0003_civil_payment_created_date_civil_payment_is_refund_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='civil_refund',
            old_name='reason',
            new_name='reason_for_refund',
        ),
        migrations.RemoveField(
            model_name='civil_bank_refund',
            name='currency',
        ),
        migrations.RemoveField(
            model_name='civil_bank_refund',
            name='iban_code',
        ),
        migrations.RemoveField(
            model_name='civil_bank_refund',
            name='refund_method',
        ),
        migrations.RemoveField(
            model_name='civil_mobile_refund',
            name='currency',
        ),
        migrations.RemoveField(
            model_name='civil_mobile_refund',
            name='refund_method',
        ),
        migrations.AddField(
            model_name='civil_bank_refund',
            name='iban_or_swift_code',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='civil_bank_refund',
            name='recipient_bank_account_number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='civil_mobile_refund',
            name='recipient_wallet_account_number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='civil_payment',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='civil_refund',
            name='currency',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='civil_refund',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='civil_refund',
            name='refund_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True),
        ),
        migrations.AddField(
            model_name='civil_refund',
            name='refund_method',
            field=models.CharField(blank=True, choices=[('bank', 'Bank'), ('mobile', 'Mobile')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='civil_refund',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Processing', 'Processing'), ('Complete', 'Complete'), ('Cancel', 'Cancel')], default='Pending', max_length=50),
        ),
        migrations.AlterField(
            model_name='civil_bank_refund',
            name='account_info',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='civil_bank_refund',
            name='additional_info',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='civil_bank_refund',
            name='recipient_bank_account_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='civil_bank_refund',
            name='recipient_bank_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='civil_bank_refund',
            name='recipient_bank_routing_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='civil_bank_refund',
            name='refund',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='civil.civil_refund'),
        ),
        migrations.AlterField(
            model_name='civil_mobile_refund',
            name='account_info',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='civil_mobile_refund',
            name='additional_info',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='civil_mobile_refund',
            name='recipient_mobile_wallet_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='civil_mobile_refund',
            name='recipient_wallet_account_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='civil_mobile_refund',
            name='refund',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='civil.civil_refund'),
        ),
        migrations.AlterField(
            model_name='civil_mobilepayment',
            name='transaction_receipt',
            field=models.ImageField(upload_to='civil/image/transaction_receipts/'),
        ),
        migrations.AlterField(
            model_name='civil_payment',
            name='currency',
            field=models.CharField(choices=[('USD', 'USD'), ('BDT', 'BDT')], default='USD', max_length=3),
        ),
        migrations.AlterField(
            model_name='civil_refund',
            name='email',
            field=models.EmailField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='civil_refund',
            name='payment',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='civil.civil_payment'),
        ),
        migrations.AlterField(
            model_name='civil_refund',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.CreateModel(
            name='Civil_OfflinePayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(max_length=100)),
                ('receipt_person_name', models.CharField(max_length=100)),
                ('receipt_person_id', models.CharField(max_length=100)),
                ('check_holder_name', models.CharField(max_length=100)),
                ('check_holder_gmail', models.EmailField(max_length=254)),
                ('check_holder_phone_number', models.CharField(max_length=14)),
                ('check_number', models.CharField(max_length=100)),
                ('check_security_code', models.CharField(max_length=100)),
                ('check_receipt', models.FileField(upload_to='civil/image/check_receipt/')),
                ('payment', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='offline_payment', to='civil.civil_payment')),
            ],
        ),
    ]
