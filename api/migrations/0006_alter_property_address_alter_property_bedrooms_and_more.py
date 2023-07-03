# Generated by Django 4.2.2 on 2023-07-03 20:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_favourite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='bedrooms',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.city'),
        ),
        migrations.AlterField(
            model_name='property',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='sale_type',
            field=models.CharField(blank=True, choices=[('Rent', 'Rent'), ('Sale', 'Sale'), ('Lease', 'Lease')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='sqft',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='state',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.state'),
        ),
        migrations.AlterField(
            model_name='property',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.propertytpe'),
        ),
    ]