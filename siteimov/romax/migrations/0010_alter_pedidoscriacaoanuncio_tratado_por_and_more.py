# Generated by Django 4.2.13 on 2024-05-11 16:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('romax', '0009_pedidoscriacaoanuncio_tratado_por_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedidoscriacaoanuncio',
            name='tratado_por',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='romax.agenteimobiliario'),
        ),
        migrations.AlterField(
            model_name='propriedade',
            name='subtipo',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Studio'), (2, 'T1'), (3, 'T2'), (4, 'T3+'), (5, 'Duplex'), (6, 'Triplex'), (7, 'Loft'), (8, 'Garden'), (9, 'Penthouse'), (10, 'Térrea'), (11, 'Vila'), (12, 'Campo'), (13, 'Praia'), (14, 'Chalé'), (15, 'Loft')]),
        ),
        migrations.AlterField(
            model_name='propriedade',
            name='tipo',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Apartamento'), (2, 'Moradia'), (3, 'Outro')]),
        ),
    ]
