# Generated by Django 4.1.4 on 2022-12-08 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_delete_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Name',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=250)),
                ('imges', models.ImageField(upload_to='pics')),
                ('descr', models.TextField()),
            ],
        ),
    ]