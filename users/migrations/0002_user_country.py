# Generated by Django 4.2.5 on 2023-10-24 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='country',
            field=models.CharField(blank=True, max_length=35, null=True, verbose_name='Страна'),
        ),
    ]