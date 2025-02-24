# Generated by Django 4.2.19 on 2025-02-19 17:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FoodItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('Dairy', 'Dairy'), ('Meat', 'Meat'), ('Vegetables', 'Vegetables'), ('Fruits', 'Fruits'), ('Grains', 'Grains'), ('Other', 'Other')], max_length=50)),
                ('quantity', models.IntegerField()),
                ('unit', models.CharField(help_text='e.g., kg, g, liters, pieces', max_length=20)),
                ('expiry_date', models.DateField()),
                ('added_on', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
