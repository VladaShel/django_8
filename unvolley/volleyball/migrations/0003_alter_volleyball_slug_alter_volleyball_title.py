# Generated by Django 4.2.1 on 2024-11-24 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volleyball', '0002_alter_volleyball_options_volleyball_slug_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volleyball',
            name='slug',
            field=models.SlugField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='volleyball',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Заголовок'),
        ),
    ]
