# Generated by Django 2.1.1 on 2018-12-28 03:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('eventName', models.CharField(max_length=64)),
                ('owner', models.CharField(max_length=32)),
                ('dayChosen', models.CharField(max_length=64)),
                ('timeChosen', models.CharField(max_length=256)),
                ('randUrl', models.CharField(max_length=20, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yourName', models.CharField(max_length=32)),
                ('freeDay', models.CharField(max_length=1024)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.Event')),
            ],
        ),
    ]
