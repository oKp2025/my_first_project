# Generated by Django 2.2.12 on 2020-11-27 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_auto_20201127_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='LastName',
            field=models.CharField(max_length=100),
        ),
    ]
