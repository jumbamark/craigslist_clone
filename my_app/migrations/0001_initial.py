# Generated by Django 3.2.3 on 2021-07-10 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search', models.CharField(max_length=500)),
                ('create', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
