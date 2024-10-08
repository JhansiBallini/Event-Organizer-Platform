# Generated by Django 4.1.7 on 2023-03-26 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_org_pg1_eservice_org_pg1_experience_org_pg1_ref_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='org_pg1',
            name='eservice',
            field=models.IntegerField(choices=[(0, 'Event Planning'), (1, 'Event Coordination'), (2, 'Event Design'), (3, 'Event Production'), (4, 'Other')], default=0),
        ),
        migrations.AlterField(
            model_name='org_pg1',
            name='etype',
            field=models.IntegerField(choices=[(0, 'Corporate'), (1, 'Wedding'), (2, 'Birthday'), (3, 'Social'), (4, 'Other')], default=0),
        ),
    ]
