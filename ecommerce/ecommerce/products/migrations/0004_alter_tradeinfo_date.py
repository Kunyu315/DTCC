# Generated by Django 4.0.6 on 2022-08-02 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_rename_name_tradeinfo_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tradeinfo',
            name='Date',
            field=models.DateField(),
        ),
    ]