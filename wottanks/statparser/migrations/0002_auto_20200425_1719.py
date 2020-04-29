# Generated by Django 3.0.4 on 2020-04-25 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statparser', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tank',
            name='economy_type',
        ),
        migrations.AddField(
            model_name='tank',
            name='is_premium',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]