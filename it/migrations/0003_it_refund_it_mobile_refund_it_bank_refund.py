# Generated by Django 5.0.2 on 2024-02-25 05:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('it', '0002_it_payment_it_mobilepayment_it_bankpayment'),
    ]

    operations = [
        migrations.CreateModel(
            name='IT_Refund',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.TextField()),
                ('proof_of_payment', models.FileField(upload_to='it/image/refund_proofs/')),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=20)),
                ('preferred_contact_method', models.CharField(blank=True, max_length=20, null=True)),
                ('additional_notes', models.TextField(blank=True, null=True)),
                ('special_instructions', models.TextField(blank=True, null=True)),
                ('feedback_or_suggestions', models.TextField(blank=True, null=True)),
                ('documentation_or_evidence', models.FileField(blank=True, null=True, upload_to='it/image/refund_documents/')),
                ('specific_issue_details', models.TextField(blank=True, null=True)),
                ('additional_comments', models.TextField(blank=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_date', models.DateTimeField(auto_now=True, null=True)),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='it.it_order')),
                ('payment', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='it.it_payment')),
            ],
        ),
        migrations.CreateModel(
            name='IT_Mobile_Refund',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency', models.CharField(max_length=10)),
                ('refund_method', models.CharField(max_length=50)),
                ('recipient_mobile_wallet_name', models.CharField(max_length=100)),
                ('recipient_wallet_account_name', models.CharField(max_length=100)),
                ('account_info', models.TextField()),
                ('additional_info', models.TextField()),
                ('refund', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='it.it_refund')),
            ],
        ),
        migrations.CreateModel(
            name='IT_Bank_Refund',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency', models.CharField(max_length=10)),
                ('refund_method', models.CharField(max_length=50)),
                ('recipient_bank_name', models.CharField(max_length=100)),
                ('recipient_bank_account_name', models.CharField(max_length=100)),
                ('recipient_bank_routing_name', models.CharField(max_length=100)),
                ('iban_code', models.CharField(max_length=100)),
                ('account_info', models.TextField()),
                ('additional_info', models.TextField()),
                ('refund', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='it.it_refund')),
            ],
        ),
    ]
