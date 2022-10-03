# Generated by Django 3.2.8 on 2022-10-03 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0003_auto_20211030_2226'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteConfiguration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(default='Site Name', max_length=255)),
                ('maintenance_mode', models.BooleanField(default=False)),
                ('twilio_callerid', models.CharField(max_length=255)),
                ('email_to', models.CharField(max_length=255)),
                ('email_from', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Site Configuration',
            },
        ),
    ]
