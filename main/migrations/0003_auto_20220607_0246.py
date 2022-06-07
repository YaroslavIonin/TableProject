# Generated by Django 3.2.9 on 2022-06-06 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20220604_1421'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='user',
        ),
        migrations.AddField(
            model_name='student',
            name='date_birth',
            field=models.DateField(null=True, verbose_name='Дата рождения'),
        ),
        migrations.AddField(
            model_name='student',
            name='in_Rus',
            field=models.BooleanField(null=True, verbose_name='Факт нахождения в России'),
        ),
        migrations.AddField(
            model_name='student',
            name='is_enrolled',
            field=models.BooleanField(null=True, verbose_name='Факт зачисления'),
        ),
    ]
