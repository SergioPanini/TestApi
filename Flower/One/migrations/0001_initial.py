# Generated by Django 3.0.5 on 2020-04-22 11:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OutSource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='APPModel',
            fields=[
                ('ID', models.IntegerField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=255)),
                ('KeyApi', models.CharField(max_length=255)),
                ('Source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='One.OutSource')),
            ],
        ),
    ]