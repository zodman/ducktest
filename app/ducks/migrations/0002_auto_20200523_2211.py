# Generated by Django 3.0.6 on 2020-05-23 22:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ducks', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ducktype',
            options={'ordering': ('name',)},
        ),
        migrations.AlterField(
            model_name='ducktype',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='foodtype',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='recorddate',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
