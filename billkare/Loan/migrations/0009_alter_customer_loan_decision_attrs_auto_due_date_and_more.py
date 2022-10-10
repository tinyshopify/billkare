# Generated by Django 4.0.5 on 2022-10-08 18:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Loan', '0008_paymentsummary_days_more_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer_loan_decision_attrs',
            name='auto_due_date',
            field=models.DateField(blank=True, db_index=True, default=datetime.date(2022, 10, 28), null=True),
        ),
        migrations.AlterField(
            model_name='customer_loan_decision_attrs',
            name='catche_bill_due_date',
            field=models.DateField(blank=True, db_index=True, default=datetime.date(2022, 11, 7), null=True),
        ),
        migrations.AlterField(
            model_name='customer_loan_decision_attrs',
            name='creditcard_due_date',
            field=models.DateField(blank=True, db_index=True, default=datetime.date(2022, 10, 28), null=True),
        ),
        migrations.AlterField(
            model_name='customer_loan_decision_attrs',
            name='mortgage_due_date',
            field=models.DateField(blank=True, default=datetime.date(2022, 10, 28), null=True),
        ),
        migrations.AlterField(
            model_name='customer_loan_decision_attrs',
            name='paycheck_date',
            field=models.DateField(blank=True, db_index=True, default=datetime.date(2022, 10, 28), null=True),
        ),
        migrations.AlterField(
            model_name='customerloan',
            name='Due_date',
            field=models.DateField(default=datetime.date(2022, 11, 7), verbose_name='Due Date'),
        ),
        migrations.AlterField(
            model_name='paymentsummary',
            name='Due_date',
            field=models.DateField(blank=True, default=datetime.date(2022, 11, 7), null=True, verbose_name='Due Date'),
        ),
        migrations.AlterField(
            model_name='paymentsummary',
            name='fund_return_date',
            field=models.DateField(default=datetime.date(2022, 11, 17), verbose_name='Fund return Date'),
        ),
        migrations.AlterField(
            model_name='paymentsummaryhistory',
            name='Due_date',
            field=models.DateField(blank=True, default=datetime.date(2022, 11, 7), null=True, verbose_name='Due Date'),
        ),
        migrations.AlterField(
            model_name='paymentsummaryhistory',
            name='fund_return_date',
            field=models.DateField(default=datetime.date(2022, 11, 17), verbose_name='Fund return Date'),
        ),
    ]
