# Generated by Django 4.0.6 on 2022-07-29 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TradeInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('Date', models.DateField(auto_now_add=True)),
                ('Open', models.DecimalField(decimal_places=6, max_digits=10)),
                ('High', models.DecimalField(decimal_places=6, max_digits=10)),
                ('Low', models.DecimalField(decimal_places=6, max_digits=10)),
                ('Close', models.DecimalField(decimal_places=6, max_digits=10)),
                ('Volume', models.IntegerField()),
            ],
            options={
                'ordering': ['Date'],
            },
        ),
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.DeleteModel(
            name='Grocery',
        ),
    ]
