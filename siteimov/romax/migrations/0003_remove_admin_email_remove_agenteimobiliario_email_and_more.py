# Generated by Django 5.0.2 on 2024-05-04 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('romax', '0002_cliente_salvos_oferta_pedidoscriacaoanuncio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admin',
            name='email',
        ),
        migrations.RemoveField(
            model_name='agenteimobiliario',
            name='email',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='email',
        ),
        migrations.AddField(
            model_name='admin',
            name='cc',
            field=models.CharField(default=0, max_length=10),
        ),
        migrations.AddField(
            model_name='admin',
            name='nif',
            field=models.PositiveBigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='admin',
            name='telemovel',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='agenteimobiliario',
            name='cc',
            field=models.CharField(default=0, max_length=10),
        ),
        migrations.AddField(
            model_name='agenteimobiliario',
            name='nif',
            field=models.PositiveBigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='agenteimobiliario',
            name='telemovel',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='cliente',
            name='cc',
            field=models.CharField(default=0, max_length=10),
        ),
        migrations.AddField(
            model_name='cliente',
            name='nif',
            field=models.PositiveBigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='cliente',
            name='telemovel',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='estadoCivil',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Solteiro'), (2, 'Casado'), (3, 'Viúvo'), (4, 'Divorciado'), (5, 'Separado judicialmente de pessoas e bens')]),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='idade',
            field=models.PositiveSmallIntegerField(blank=True),
        ),
    ]
