# Generated by Django 4.0 on 2022-03-20 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0009_rename_blogmod_commentmodel_blogmodel_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogmodel',
            name='summary',
            field=models.TextField(blank=True, max_length=50),
        ),
    ]
