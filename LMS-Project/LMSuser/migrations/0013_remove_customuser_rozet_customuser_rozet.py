# Generated by Django 4.2.5 on 2023-11-09 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LMSuser', '0012_rozetler_customuser_rozet'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='rozet',
        ),
        migrations.AddField(
            model_name='customuser',
            name='rozet',
            field=models.ManyToManyField(to='LMSuser.rozetler'),
        ),
    ]
