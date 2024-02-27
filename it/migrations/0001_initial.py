# Generated by Django 5.0.2 on 2024-02-27 11:50

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('it_dashboard', '__first__'),
        ('user', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='IT_Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=300)),
                ('project_file', models.FileField(blank=True, null=True, upload_to='it/order/project-file/')),
                ('related_file', models.FileField(blank=True, null=True, upload_to='it/order/related-file/')),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Payment', 'Payment'), ('Waiting', 'Waiting'), ('Working', 'Working'), ('Complited', 'Complited'), ('Cancel', 'Cancel')], max_length=40)),
                ('piority', models.CharField(choices=[('Normal', 'Normal'), ('Medium', 'Medium'), ('Emergency', 'Emergency')], max_length=40)),
                ('currency', models.CharField(blank=True, choices=[('USD', 'USD'), ('BDT', 'BDT'), ('INR', 'INR'), ('EUR', 'EUR'), ('GBP', 'GBP'), ('CAD', 'CAD')], max_length=20, null=True)),
                ('total_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('total_online_deposite', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('total_offline_deposite', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('total_amount_paid', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('total_amount_remain', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('profit_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('delivery_date', models.DateField(blank=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='it_order', to='user.website_user')),
            ],
            options={
                'ordering': ['updated_date', 'created_date', 'delivery_date'],
            },
        ),
        migrations.CreateModel(
            name='IT_Order_Admin_Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_box', models.TextField(blank=True, null=True)),
                ('file_or_image', models.FileField(blank=True, null=True, upload_to='it/order/note-file/')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='it_order_note', to='it.it_order')),
            ],
        ),
        migrations.CreateModel(
            name='IT_Order_Update_Box',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True, null=True)),
                ('time', models.TimeField(auto_now_add=True, null=True)),
                ('seen', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='it_order_update', to='it.it_order')),
            ],
            options={
                'ordering': ('timestamp',),
            },
        ),
        migrations.CreateModel(
            name='IT_Order_User_Information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, max_length=10, null=True)),
                ('nationality', models.CharField(blank=True, max_length=255, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('email_address', models.EmailField(blank=True, max_length=254, null=True)),
                ('home_address', models.TextField(blank=True, null=True)),
                ('educational_qualifications', models.TextField(blank=True, null=True)),
                ('professional_details', models.TextField(blank=True, null=True)),
                ('occupation', models.CharField(blank=True, max_length=255, null=True)),
                ('work_experience', models.IntegerField(blank=True, null=True)),
                ('skills', models.TextField(blank=True, null=True)),
                ('interests', models.TextField(blank=True, null=True)),
                ('hobbies', models.TextField(blank=True, null=True)),
                ('profile_id', models.CharField(blank=True, max_length=50, null=True)),
                ('application_date', models.DateField(auto_now_add=True)),
                ('user_photo', models.ImageField(blank=True, null=True, upload_to='it/order/user/')),
                ('user_signature', models.ImageField(blank=True, null=True, upload_to='it/order/user/signature/')),
                ('company_signature', models.ImageField(blank=True, null=True, upload_to='it/order/company/signature/')),
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='it_order_user_information', to='it.it_order')),
            ],
        ),
        migrations.CreateModel(
            name='IT_Order_Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=255)),
                ('brand', models.CharField(max_length=255)),
                ('color', models.CharField(max_length=20)),
                ('size', models.CharField(max_length=10)),
                ('order_profile_information', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='it_order_product', to='it.it_order_user_information')),
            ],
        ),
        migrations.CreateModel(
            name='IT_Order_Work_Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_box', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='it/order/work-update/')),
                ('files', models.FileField(blank=True, null=True, upload_to='it/order/work-update/')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='it_order_work_document', to='it.it_order')),
            ],
        ),
        migrations.CreateModel(
            name='IT_Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency', models.CharField(blank=True, choices=[('USD', 'USD'), ('BDT', 'BDT')], max_length=3, null=True)),
                ('payment_amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('payment_type', models.CharField(blank=True, choices=[('Online', 'Online'), ('Offline', 'Offline')], max_length=10, null=True)),
                ('payment_method', models.CharField(blank=True, choices=[('bank', 'Bank'), ('mobile', 'Mobile')], max_length=10, null=True)),
                ('is_varified', models.BooleanField(default=False)),
                ('is_refund', models.BooleanField(default=False)),
                ('status', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_date', models.DateTimeField(auto_now=True, null=True)),
                ('bank', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='it_bank', to='it_dashboard.it_bank')),
                ('mobile_wallet', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='it_mobile_wallet', to='it_dashboard.it_mobilewallet')),
                ('order', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='it_order_payment', to='it.it_order')),
            ],
        ),
        migrations.CreateModel(
            name='IT_OfflinePayment',
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
                ('check_receipt', models.FileField(upload_to='it/image/check_receipt/')),
                ('is_varified', models.BooleanField(default=False)),
                ('payment', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='offline_payment', to='it.it_payment')),
            ],
        ),
        migrations.CreateModel(
            name='IT_MobilePayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_holder_name', models.CharField(max_length=100)),
                ('account_holder_email', models.EmailField(max_length=254)),
                ('account_holder_phone', models.CharField(max_length=15)),
                ('mobile_wallet_name', models.CharField(max_length=100)),
                ('account_type', models.CharField(max_length=100)),
                ('account_info', models.TextField()),
                ('transaction_id', models.CharField(max_length=100, unique=True)),
                ('transaction_receipt', models.ImageField(upload_to='it/image/transaction_receipts/')),
                ('agree', models.BooleanField()),
                ('payment', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='mobile_payment', to='it.it_payment')),
            ],
        ),
        migrations.CreateModel(
            name='IT_BankPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_holder_name', models.CharField(max_length=100)),
                ('account_holder_email', models.EmailField(max_length=254)),
                ('account_holder_phone', models.CharField(max_length=15)),
                ('bank_name', models.CharField(max_length=100)),
                ('account_number', models.CharField(max_length=50)),
                ('account_info', models.TextField(blank=True)),
                ('transaction_id', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('transaction_receipt', models.ImageField(upload_to='it/image/transaction_receipts/')),
                ('additional_info', models.TextField(blank=True)),
                ('agree', models.BooleanField()),
                ('payment', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='bank_payment', to='it.it_payment')),
            ],
        ),
        migrations.CreateModel(
            name='IT_Refund',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('refund_method', models.CharField(blank=True, choices=[('bank', 'Bank'), ('mobile', 'Mobile')], max_length=50, null=True)),
                ('currency', models.CharField(blank=True, max_length=10, null=True)),
                ('refund_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Processing', 'Processing'), ('Complete', 'Complete'), ('Cancel', 'Cancel')], default='Pending', max_length=50)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('preferred_contact_method', models.CharField(blank=True, max_length=20, null=True)),
                ('reason_for_refund', models.TextField()),
                ('proof_of_payment', models.FileField(upload_to='it/image/refund_proofs/')),
                ('additional_notes', models.TextField(blank=True, null=True)),
                ('special_instructions', models.TextField(blank=True, null=True)),
                ('feedback_or_suggestions', models.TextField(blank=True, null=True)),
                ('documentation_or_evidence', models.FileField(blank=True, null=True, upload_to='it/image/refund_documents/')),
                ('specific_issue_details', models.TextField(blank=True, null=True)),
                ('additional_comments', models.TextField(blank=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_date', models.DateTimeField(auto_now=True, null=True)),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='it.it_order')),
                ('payment', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='it.it_payment')),
            ],
        ),
        migrations.CreateModel(
            name='IT_Mobile_Refund',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipient_mobile_wallet_name', models.CharField(blank=True, max_length=100, null=True)),
                ('recipient_wallet_account_name', models.CharField(blank=True, max_length=100, null=True)),
                ('recipient_wallet_account_number', models.CharField(blank=True, max_length=100, null=True)),
                ('account_info', models.TextField(blank=True, null=True)),
                ('additional_info', models.TextField(blank=True, null=True)),
                ('refund', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='it.it_refund')),
            ],
        ),
        migrations.CreateModel(
            name='IT_Bank_Refund',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipient_bank_name', models.CharField(blank=True, max_length=100, null=True)),
                ('recipient_bank_account_name', models.CharField(blank=True, max_length=100, null=True)),
                ('recipient_bank_account_number', models.CharField(blank=True, max_length=100, null=True)),
                ('recipient_bank_routing_name', models.CharField(blank=True, max_length=100, null=True)),
                ('iban_or_swift_code', models.CharField(blank=True, max_length=100, null=True)),
                ('account_info', models.TextField(blank=True, null=True)),
                ('additional_info', models.TextField(blank=True, null=True)),
                ('refund', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='it.it_refund')),
            ],
        ),
    ]
