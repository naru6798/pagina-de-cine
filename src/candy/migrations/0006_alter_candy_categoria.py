# Generated by Django 5.1.7 on 2025-04-02 22:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candy', '0005_alter_candy_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candy',
            name='categoria',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='candy.categoriacandy'),
        ),
    ]
