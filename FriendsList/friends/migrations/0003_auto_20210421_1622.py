# Generated by Django 3.1.6 on 2021-04-21 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('friends', '0002_category_counter'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='counter',
            field=models.PositiveIntegerField(default=0, help_text='counts number of category', unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='counter',
            field=models.PositiveIntegerField(help_text='counts number of category', unique=True),
        ),
    ]
