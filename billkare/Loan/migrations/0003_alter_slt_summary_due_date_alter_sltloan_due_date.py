# Generated by Django 4.0.5 on 2022-09-09 05:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Loan', '0002_alter_slt_summary_due_date_alter_sltloan_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slt_summary',
            name='Due_date',
            field=models.DateField(default=datetime.date(2022, 9, 29), verbose_name='Due Date'),
        ),
        migrations.AlterField(
            model_name='sltloan',
            name='Due_date',
            field=models.DateField(default=datetime.date(2022, 9, 29), verbose_name='Due Date'),
        ),
    ]