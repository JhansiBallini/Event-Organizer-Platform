# Generated by Django 4.1.7 on 2023-03-27 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0007_alter_org_pg1_eservice_alter_org_pg1_etype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='org_pg1',
            name='eservice',
            field=models.BooleanField(default='False'),
        ),
        migrations.AlterField(
            model_name='org_pg1',
            name='etype',
            field=models.BooleanField(default='False'),
        ),
    ]
