# Generated by Django 2.2 on 2023-03-09 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0003_auto_20230309_1213'),
    ]

    operations = [
        migrations.AddField(
            model_name='color',
            name='rgb_code',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
