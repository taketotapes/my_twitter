# Generated by Django 5.0 on 2023-12-26 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=128)),
                ('first_name', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=128)),
                ('date_joined', models.DateField(auto_now_add=True)),
            ],
        ),
    ]