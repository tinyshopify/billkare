# Generated by Django 4.0.5 on 2022-09-30 16:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Loan', '0006_alter_customer_loan_decision_attrs_auto_due_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentsummary',
            name='Due_date',
            field=models.DateField(blank=True, default=datetime.date(2022, 10, 30), null=True, verbose_name='Due Date'),
        ),
        migrations.AddField(
            model_name='paymentsummaryhistory',
            name='Due_date',
            field=models.DateField(blank=True, default=datetime.date(2022, 10, 30), null=True, verbose_name='Due Date'),
        ),
    ]