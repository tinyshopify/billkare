# Generated by Django 4.0.5 on 2022-10-09 12:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Loan', '0009_alter_customer_loan_decision_attrs_auto_due_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paymentinfo',
            old_name='Payment_address',
            new_name='company',
        ),
        migrations.RemoveField(
            model_name='paymentinfo',
            name='Due_date',
        ),
        migrations.AddField(
            model_name='paymentinfo',
            name='country',
            field=models.CharField(default=0, max_length=50),
        ),
        migrations.AddField(
            model_name='paymentinfo',
            name='firstname',
            field=models.CharField(default=0, max_length=50),
        ),
        migrations.AddField(
            model_name='paymentinfo',
            name='lastname',
            field=models.CharField(default=0, max_length=50),
        ),
        migrations.AddField(
            model_name='paymentinfo',
            name='state',
            field=models.CharField(default=0, max_length=50),
        ),
        migrations.AddField(
            model_name='paymentinfo',
            name='street',
            field=models.CharField(default=0, max_length=50),
        ),
        migrations.AddField(
            model_name='paymentinfo',
            name='zip',
            field=models.CharField(default=0, max_length=50),
        ),
        migrations.AlterField(
            model_name='customer_loan_decision_attrs',
            name='auto_due_date',
            field=models.DateField(blank=True, db_index=True, default=datetime.date(2022, 10, 29), null=True),
        ),
        migrations.AlterField(
            model_name='customer_loan_decision_attrs',
            name='catche_bill_due_date',
            field=models.DateField(blank=True, db_index=True, default=datetime.date(2022, 11, 8), null=True),
        ),
        migrations.AlterField(
            model_name='customer_loan_decision_attrs',
            name='creditcard_due_date',
            field=models.DateField(blank=True, db_index=True, default=datetime.date(2022, 10, 29), null=True),
        ),
        migrations.AlterField(
            model_name='customer_loan_decision_attrs',
            name='mortgage_due_date',
            field=models.DateField(blank=True, default=datetime.date(2022, 10, 29), null=True),
        ),
        migrations.AlterField(
            model_name='customer_loan_decision_attrs',
            name='paycheck_date',
            field=models.DateField(blank=True, db_index=True, default=datetime.date(2022, 10, 29), null=True),
        ),
        migrations.AlterField(
            model_name='customerloan',
            name='Due_date',
            field=models.DateField(default=datetime.date(2022, 11, 8), verbose_name='Due Date'),
        ),
        migrations.AlterField(
            model_name='paymentsummary',
            name='Due_date',
            field=models.DateField(blank=True, default=datetime.date(2022, 11, 8), null=True, verbose_name='Due Date'),
        ),
        migrations.AlterField(
            model_name='paymentsummary',
            name='fund_return_date',
            field=models.DateField(default=datetime.date(2022, 11, 18), verbose_name='Fund return Date'),
        ),
        migrations.AlterField(
            model_name='paymentsummaryhistory',
            name='Due_date',
            field=models.DateField(blank=True, default=datetime.date(2022, 11, 8), null=True, verbose_name='Due Date'),
        ),
        migrations.AlterField(
            model_name='paymentsummaryhistory',
            name='fund_return_date',
            field=models.DateField(default=datetime.date(2022, 11, 18), verbose_name='Fund return Date'),
        ),
    ]
