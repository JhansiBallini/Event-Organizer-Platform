# Generated by Django 4.1.7 on 2023-04-03 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0018_remove_organizers_epic'),
    ]

    operations = [
        migrations.AddField(
            model_name='organizers',
            name='epic',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
