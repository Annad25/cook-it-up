# Generated by Django 4.2 on 2023-04-22 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_recipe_recipe_ingredients'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Uname', models.CharField(max_length=250)),
                ('Email', models.CharField(max_length=250)),
            ],
        ),
    ]
