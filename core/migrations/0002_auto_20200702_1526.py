# Generated by Django 3.0.7 on 2020-07-02 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='notes',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='appointment',
            name='recieved',
            field=models.BooleanField(default=False),
        ),
    ]
