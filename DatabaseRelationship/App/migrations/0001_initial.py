# Generated by Django 2.1 on 2018-08-24 20:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flower',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('color', models.CharField(max_length=100)),
                ('description', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Garden',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(default='')),
            ],
        ),
        migrations.AddField(
            model_name='flower',
            name='garden',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.Garden'),
        ),
    ]