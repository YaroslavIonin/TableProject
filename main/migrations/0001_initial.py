# Generated by Django 3.2.9 on 2022-05-26 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_ru', models.CharField(max_length=255, verbose_name='Фио на русском языке')),
                ('name_en', models.CharField(max_length=255, verbose_name='Фио на английском языке')),
                ('country', models.CharField(max_length=255, verbose_name='Страна')),
                ('number_doc', models.BigIntegerField(blank=True, verbose_name='Номер документа')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')),
                ('gender', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='main.gender', verbose_name='Пол')),
            ],
        ),
    ]
