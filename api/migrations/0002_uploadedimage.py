# Generated by Django 4.2.2 on 2023-07-21 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadedImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_image', models.ImageField(upload_to='house_uploads/')),
                ('thumbnail_image', models.ImageField(blank=True, upload_to='house_uploads/thumbnails/')),
                ('medium_image', models.ImageField(blank=True, upload_to='house_uploads/medium/')),
                ('large_image', models.ImageField(blank=True, upload_to='house_uploads/large/')),
            ],
        ),
    ]
