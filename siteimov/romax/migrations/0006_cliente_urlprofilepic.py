# Generated by Django 5.0.2 on 2024-05-07 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('romax', '0005_alter_cliente_telemovel'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='urlprofilepic',
            field=models.URLField(default=''),
        ),
    ]
