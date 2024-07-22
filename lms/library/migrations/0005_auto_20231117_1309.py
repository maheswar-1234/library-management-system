# Generated by Django 3.0 on 2023-11-17 07:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_transaction'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transactionn',
            fields=[
                ('transactionid', models.IntegerField(primary_key=True, serialize=False)),
                ('receiveddate', models.DateField(null=True)),
                ('submissiondate', models.DateField(null=True)),
                ('bookid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.Book')),
                ('sid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.Receiver')),
            ],
        ),
        migrations.DeleteModel(
            name='Transaction',
        ),
    ]
