# Generated by Django 4.1.3 on 2022-12-02 06:57

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
            name='plaidUser',
            fields=[
                ('isActive', models.BooleanField(db_index=True, default=True)),
                ('creUser', models.CharField(db_index=True, default=None, max_length=50)),
                ('CreatedTs', models.DateTimeField(db_index=True, null=True)),
                ('UpdateTs', models.DateTimeField(db_index=True, null=True)),
                ('creDate', models.DateTimeField(auto_now_add=True, db_index=True, null=True)),
                ('InsUpdFlag', models.CharField(db_index=True, max_length=50, null=True)),
                ('plaid_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('access_token', models.CharField(blank=True, max_length=50)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('Sugan_id', models.ForeignKey(default=uuid.uuid4, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='plaidUserHistory',
            fields=[
                ('isActive', models.BooleanField(db_index=True, default=True)),
                ('creUser', models.CharField(db_index=True, default=None, max_length=50)),
                ('CreatedTs', models.DateTimeField(db_index=True, null=True)),
                ('UpdateTs', models.DateTimeField(db_index=True, null=True)),
                ('creDate', models.DateTimeField(auto_now_add=True, db_index=True, null=True)),
                ('InsUpdFlag', models.CharField(db_index=True, max_length=50, null=True)),
                ('EventID', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('access_token', models.CharField(blank=True, max_length=50, null=True)),
                ('linkReason', models.CharField(blank=True, max_length=50)),
                ('StartDate', models.DateTimeField(auto_now_add=True)),
                ('EndDate', models.DateTimeField(auto_now_add=True)),
                ('Sugan_id', models.ForeignKey(default=uuid.uuid4, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('plaid_id', models.ForeignKey(default=uuid.uuid4, on_delete=django.db.models.deletion.CASCADE, to='plaidlink.plaiduser')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
