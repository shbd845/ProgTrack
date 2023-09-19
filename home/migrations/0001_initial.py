# Generated by Django 4.2.5 on 2023-09-19 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskTitle', models.CharField(max_length=50)),
                ('taskDesc', models.TextField()),
                ('Time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
