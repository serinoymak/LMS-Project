# Generated by Django 4.2.5 on 2023-11-09 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LMSapp', '0007_remove_altcategory_alt_ana_kategori_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='altcategory',
            name='ana_category',
            field=models.ManyToManyField(related_name='category', to='LMSapp.anacategory'),
        ),
    ]
