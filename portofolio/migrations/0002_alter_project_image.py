# Generated by Django 3.2.9 on 2021-11-23 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portofolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(upload_to='static/images/'),
        ),
    ]