# Generated by Django 5.0.2 on 2024-02-26 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('civil', '0005_civil_offlinepayment_is_varified_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='civil_order_user_information',
            name='payment_currency',
        ),
        migrations.AlterField(
            model_name='civil_order_user_information',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='civil_order_user_information',
            name='educational_qualifications',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='civil_order_user_information',
            name='email_address',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='civil_order_user_information',
            name='gender',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='civil_order_user_information',
            name='hobbies',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='civil_order_user_information',
            name='home_address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='civil_order_user_information',
            name='interests',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='civil_order_user_information',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='civil_order_user_information',
            name='nationality',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='civil_order_user_information',
            name='occupation',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='civil_order_user_information',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='civil_order_user_information',
            name='professional_details',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='civil_order_user_information',
            name='skills',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='civil_order_user_information',
            name='work_experience',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
