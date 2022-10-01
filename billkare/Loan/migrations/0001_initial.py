# Generated by Django 4.0.5 on 2022-09-27 11:22

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='customer_loan_decision_attrs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isActive', models.BooleanField(db_index=True, default=True)),
                ('creUser', models.CharField(db_index=True, default=None, max_length=50)),
                ('CreatedTs', models.DateTimeField(db_index=True, null=True)),
                ('UpdateTs', models.DateTimeField(db_index=True, null=True)),
                ('creDate', models.DateTimeField(auto_now_add=True, db_index=True, null=True)),
                ('InsUpdFlag', models.CharField(db_index=True, max_length=50, null=True)),
                ('balance', models.FloatField(default=0)),
                ('loanType', models.CharField(db_index=True, default=None, max_length=50)),
                ('mortgage_due_amount', models.FloatField(default=0)),
                ('mortgage_due_date', models.DateTimeField(default=datetime.date(2022, 10, 17))),
                ('auto_loan_amount', models.FloatField(default=0)),
                ('auto_due_date', models.DateTimeField(db_index=True, default=datetime.date(2022, 10, 17), null=True)),
                ('creditcard_min_paydue_amount', models.FloatField(default=0)),
                ('creditcard_statment_balance_amount', models.FloatField(default=0)),
                ('creditcard_due_date', models.DateTimeField(db_index=True, default=datetime.date(2022, 10, 17), null=True)),
                ('loan_eligiblity_flag', models.CharField(db_index=True, default=None, max_length=50)),
                ('max_loan_amount_from_catche', models.FloatField(default=0)),
                ('min_loan_amount_from_catche', models.FloatField(default=0)),
                ('estimated_balance', models.FloatField(default=0)),
                ('shortage_bill_amount', models.FloatField(default=0)),
                ('paycheck_date', models.DateTimeField(db_index=True, default=datetime.date(2022, 10, 17), null=True)),
                ('catche_risk_score_0_100', models.IntegerField(default=0)),
                ('customer_entered_bill_amount', models.FloatField(default=0)),
                ('catche_bill_due_date', models.DateTimeField(db_index=True, default=datetime.date(2022, 10, 27), null=True)),
                ('catche_id', models.ForeignKey(default=uuid.uuid4, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
