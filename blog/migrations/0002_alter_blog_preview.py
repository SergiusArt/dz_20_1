# Generated by Django 4.2.5 on 2023-09-24 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='preview',
            field=models.ImageField(blank=True, null=True, upload_to='blog/media/blog/blog', verbose_name='Превью'),
        ),
    ]
