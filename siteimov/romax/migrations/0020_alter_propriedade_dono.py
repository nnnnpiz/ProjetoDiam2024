# Generated by Django 4.2.13 on 2024-05-12 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('romax', '0019_alter_propriedade_dono'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propriedade',
            name='dono',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='romax.cliente'),
        ),
    ]
