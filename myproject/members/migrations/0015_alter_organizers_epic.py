# Generated by Django 4.1.7 on 2023-04-03 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0014_alter_organizers_epic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizers',
            name='epic',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
