# Generated by Django 3.0 on 2023-11-16 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('authorid', models.IntegerField(primary_key=True, serialize=False)),
                ('authorname', models.CharField(max_length=100)),
            ],
        ),
    ]