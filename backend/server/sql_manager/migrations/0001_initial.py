# Generated by Django 5.0.2 on 2024-03-04 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TTT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('hp', models.IntegerField()),
                ('attack', models.IntegerField()),
                ('defense', models.IntegerField()),
                ('spattack', models.IntegerField()),
                ('spdefense', models.IntegerField()),
                ('speed', models.IntegerField()),
                ('type1', models.CharField(max_length=50)),
                ('type2', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'ttt',
            },
        ),
    ]
