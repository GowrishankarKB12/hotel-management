# Generated by Django 2.0.4 on 2018-04-09 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='dob',
            new_name='ad',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='password',
            new_name='nr',
        ),
        migrations.AddField(
            model_name='user',
            name='dd',
            field=models.DateField(blank=True, null=True),
        ),
    ]
