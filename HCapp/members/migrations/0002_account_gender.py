# Generated by Django 4.1.7 on 2023-03-20 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='Gender',
            field=models.CharField(default='Male', max_length=10, null=True),
        ),
    ]