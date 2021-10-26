# Generated by Django 3.2.4 on 2021-10-22 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.TextField(max_length=50)),
                ('position', models.TextField(max_length=50)),
                ('office', models.TextField(max_length=50)),
                ('salary', models.IntegerField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-updated'],
            },
        ),
    ]
