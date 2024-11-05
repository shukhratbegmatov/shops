# Generated by Django 4.1.7 on 2023-03-28 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system_settings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='logo',
            field=models.FileField(blank=True, null=True, upload_to='organization/logo'),
        ),
        migrations.AddField(
            model_name='organization',
            name='subdomain_field',
            field=models.SlugField(default='', max_length=200),
        ),
    ]
