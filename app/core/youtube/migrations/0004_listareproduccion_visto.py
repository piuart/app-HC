# Generated by Django 2.2.14 on 2021-04-12 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtube', '0003_remove_listareproduccion_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='listareproduccion',
            name='visto',
            field=models.BooleanField(default=False),
        ),
    ]
