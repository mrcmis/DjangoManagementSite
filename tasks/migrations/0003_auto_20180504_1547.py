# Generated by Django 2.0.4 on 2018-05-04 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_auto_20180413_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.CharField(choices=[('LOW', 'Low'), ('MED', 'Medium'), ('HIG', 'High'), ('CRI', 'Critical')], default='LOW', max_length=3),
        ),
    ]