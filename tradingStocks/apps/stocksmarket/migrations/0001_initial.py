# Generated by Django 4.1.9 on 2023-09-16 22:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_created', models.DateTimeField(auto_now_add=True, verbose_name='время создания')),
                ('datetime_updated', models.DateTimeField(auto_now=True, verbose_name='время обновления')),
                ('datetime_deleted', models.DateTimeField(blank=True, null=True, verbose_name='время удаления')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('price_per_share', models.DecimalField(decimal_places=2, max_digits=20)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('action', models.CharField(max_length=255)),
                ('symbol', models.CharField(max_length=255)),
                ('quantity', models.IntegerField()),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Транзакция',
                'verbose_name_plural': 'Транзакции',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Holding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_created', models.DateTimeField(auto_now_add=True, verbose_name='время создания')),
                ('datetime_updated', models.DateTimeField(auto_now=True, verbose_name='время обновления')),
                ('datetime_deleted', models.DateTimeField(blank=True, null=True, verbose_name='время удаления')),
                ('title', models.CharField(max_length=100)),
                ('price_per_share', models.DecimalField(decimal_places=2, max_digits=20)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('symbol', models.CharField(max_length=255)),
                ('quantity', models.IntegerField()),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Актив',
                'verbose_name_plural': 'Активы',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_created', models.DateTimeField(auto_now_add=True, verbose_name='время создания')),
                ('datetime_updated', models.DateTimeField(auto_now=True, verbose_name='время обновления')),
                ('datetime_deleted', models.DateTimeField(blank=True, null=True, verbose_name='время удаления')),
                ('account', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]