# Generated by Django 4.2.7 on 2023-11-27 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categoria',
            old_name='nobre',
            new_name='nombre',
        ),
        migrations.AlterField(
            model_name='post',
            name='detalle',
            field=models.CharField(max_length=100),
        ),
    ]