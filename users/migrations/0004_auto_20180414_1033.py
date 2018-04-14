# Generated by Django 2.0.4 on 2018-04-14 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20180414_1026'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='age',
        ),
        migrations.AddField(
            model_name='person',
            name='date_of_birth',
            field=models.DateField(default='1900-01-01'),
        ),
        migrations.AlterField(
            model_name='person',
            name='position',
            field=models.CharField(choices=[('BOS', 'Boss'), ('MAN', 'Manager'), ('SUP', 'Supervisor'), ('WOR', 'Worker')], default='WOR', max_length=3),
        ),
    ]