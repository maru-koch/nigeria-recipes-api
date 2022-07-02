# Generated by Django 4.0.5 on 2022-07-02 17:03

import api.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Preparation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('duration', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='images')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=500)),
                ('preparation', models.TextField(max_length=500, verbose_name=api.models.Preparation)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.category')),
                ('ingredients', models.ManyToManyField(blank=True, null=True, related_name='meals', to='api.ingredients')),
            ],
        ),
    ]
