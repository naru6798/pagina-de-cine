# Generated by Django 5.1.7 on 2025-04-02 22:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candy', '0003_alter_candy_precio'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaCandy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='candy',
            name='categoria',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='candy.categoriacandy'),
        ),
    ]
