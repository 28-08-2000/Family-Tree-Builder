# Generated by Django 3.0.6 on 2022-03-08 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('create', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='individual',
            name='offspring',
            field=models.ManyToManyField(blank=True, null=True, related_name='offsprings', to='create.individual'),
        ),
        migrations.AddField(
            model_name='individual',
            name='parent',
            field=models.ManyToManyField(blank=True, null=True, related_name='parents', to='create.individual'),
        ),
    ]
