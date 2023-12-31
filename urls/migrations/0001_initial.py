# Generated by Django 4.2.6 on 2023-10-13 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='URL',
            fields=[
                ('Full_url', models.URLField()),
                ('name', models.CharField(max_length=255)),
                ('clicks', models.IntegerField(default=0)),
                ('shorturl', models.CharField(editable=False, max_length=5, primary_key=True, serialize=False, unique=True)),
            ],
        ),
    ]
