# Generated by Django 3.0 on 2020-01-26 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Имя')),
                ('mail', models.EmailField(default=0, max_length=254, verbose_name='E-mail')),
                ('school', models.IntegerField(default=0, verbose_name='Школа')),
                ('level', models.IntegerField(default=0, verbose_name='Класс')),
                ('password', models.CharField(max_length=50, verbose_name='Пароль')),
                ('fiscul', models.BooleanField(default=False, verbose_name='Физ-ра')),
                ('lit', models.BooleanField(default=False, verbose_name='Литература')),
                ('algebra', models.BooleanField(default=False, verbose_name='Алгебра')),
                ('geomet', models.BooleanField(default=False, verbose_name='Геометрия')),
                ('history', models.BooleanField(default=False, verbose_name='История')),
                ('fiscul_t', models.FloatField(blank=True, default=None, null=True, verbose_name='Физ-ра--цель')),
                ('lit_t', models.FloatField(blank=True, default=None, null=True, verbose_name='Литература--цель')),
                ('algebra_t', models.FloatField(blank=True, default=None, null=True, verbose_name='Алгебра--цель')),
                ('geomet_t', models.FloatField(blank=True, default=None, null=True, verbose_name='Геометрия--цель')),
                ('history_t', models.FloatField(blank=True, default=None, null=True, verbose_name='История--цель')),
            ],
        ),
    ]
