# Generated by Django 3.2.5 on 2021-08-22 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentlist', '0002_auto_20210822_0616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='firstname',
            field=models.CharField(max_length=20),
        ),
    ]
