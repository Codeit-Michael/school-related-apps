# Generated by Django 3.2.5 on 2021-08-22 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentlist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='age',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='firstname',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='student',
            name='lastname',
            field=models.CharField(default='', max_length=20),
        ),
    ]
