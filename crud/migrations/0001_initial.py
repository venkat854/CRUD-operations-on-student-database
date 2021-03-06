# Generated by Django 3.2 on 2021-06-09 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClientInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=10)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'ClientInfo',
                'verbose_name_plural': 'ClientInfo',
            },
        ),
    ]
