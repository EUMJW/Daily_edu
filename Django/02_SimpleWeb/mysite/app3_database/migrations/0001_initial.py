# Generated by Django 3.0.7 on 2020-06-08 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestClass',
            fields=[
                ('test_idx', models.AutoField(primary_key=True, serialize=False)),
                ('test_str', models.TextField()),
                ('test_int', models.IntegerField()),
            ],
        ),
    ]
