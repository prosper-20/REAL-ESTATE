# Generated by Django 4.2.2 on 2023-07-07 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='sender',
            field=models.CharField(max_length=100),
        ),
    ]
