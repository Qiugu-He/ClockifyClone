# Generated by Django 3.1 on 2020-08-23 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_no', models.CharField(max_length=32, unique=True)),
                ('task_desc', models.CharField(max_length=32)),
            ],
        ),
    ]
