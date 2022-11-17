# Generated by Django 4.0.5 on 2022-11-16 08:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Loan', '0002_customer_loan_decision_attrs_upload_statement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer_loan_decision_attrs',
            name='Upload_statement',
            field=models.FileField(null=True, upload_to='uploads/loanstatements/', validators=[django.core.validators.FileExtensionValidator(['pdf'])]),
        ),
        migrations.AlterField(
            model_name='customer_loan_decision_attrs',
            name='loan_eligiblity_flag',
            field=models.CharField(blank=True, db_index=True, max_length=50, null=True),
        ),
    ]