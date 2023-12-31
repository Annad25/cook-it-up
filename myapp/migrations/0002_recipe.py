# Generated by Django 4.2 on 2023-04-19 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_name', models.CharField(max_length=250)),
                ('recipe_description', models.TextField()),
                ('recipe_image', models.ImageField(upload_to='recipe')),
            ],
            options={
                'verbose_name_plural': 'Recipe Table',
            },
        ),
    ]
