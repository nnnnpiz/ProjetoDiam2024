# Generated by Django 5.0.4 on 2024-05-12 14:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('romax', '0015_alter_pedidoscriacaoanuncio_data_fecho_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedidoscriacaoanuncio',
            name='tratado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='romax.agenteimobiliario'),
        ),
    ]
