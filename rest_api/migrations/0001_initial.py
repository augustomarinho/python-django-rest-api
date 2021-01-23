# Generated by Django 3.1.5 on 2021-01-23 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('document', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('training_code', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=100)),
                ('level', models.CharField(choices=[('B', 'BASIC'), ('I', 'INTERMEDIATE'), ('A', 'ADVANCED')], default='B', max_length=1)),
            ],
        ),
    ]
