# Generated by Django 4.0.5 on 2022-08-21 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0028_statutes_sec_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadcasefile',
            name='uploadfile_short_desc',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]