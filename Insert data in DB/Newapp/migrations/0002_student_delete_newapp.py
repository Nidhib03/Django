# Generated by Django 4.0.3 on 2022-03-10 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('name', models.CharField(db_column='name', max_length=20)),
                ('branch', models.CharField(db_column='branch', max_length=20)),
                ('roll', models.IntegerField(db_column='roll')),
                ('age', models.IntegerField()),
            ],
            options={
                'db_table': 'Person',
            },
        ),
        migrations.DeleteModel(
            name='Newapp',
        ),
    ]
