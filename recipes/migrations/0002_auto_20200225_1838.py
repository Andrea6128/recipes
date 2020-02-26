# Generated by Django 3.0.2 on 2020-02-25 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='mealComments',
        ),
        migrations.AlterField(
            model_name='recipe',
            name='mealCalories',
            field=models.PositiveIntegerField(blank=True, verbose_name='Calories'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='mealCookTime',
            field=models.PositiveIntegerField(blank=True, verbose_name='Cooking Time'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='mealDirections',
            field=models.TextField(blank=True, max_length=500, verbose_name='Directions'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='mealRate',
            field=models.PositiveIntegerField(blank=True, verbose_name='Rating'),
        ),
    ]
