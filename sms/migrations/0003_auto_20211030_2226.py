# Generated by Django 3.2.8 on 2021-10-30 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0002_auto_20211030_2215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='When'),
        ),
        migrations.AlterField(
            model_name='message',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='Id'),
        ),
        migrations.AlterField(
            model_name='message',
            name='message_body',
            field=models.TextField(verbose_name='Text of message'),
        ),
        migrations.AlterField(
            model_name='message',
            name='message_from',
            field=models.CharField(max_length=200, verbose_name='From'),
        ),
        migrations.AlterField(
            model_name='message',
            name='message_to',
            field=models.CharField(max_length=200, verbose_name='To'),
        ),
    ]
