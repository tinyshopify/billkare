# Generated by Django 4.0.5 on 2022-10-08 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plaidlink', '0002_alter_plaiduserhistory_access_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plaiduserhistory',
            name='access_token',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
