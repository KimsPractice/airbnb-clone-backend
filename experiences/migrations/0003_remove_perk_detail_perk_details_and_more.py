# Generated by Django 4.1.7 on 2023-03-15 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experiences', '0002_rename_experiencs_experience'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perk',
            name='detail',
        ),
        migrations.AddField(
            model_name='perk',
            name='details',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='perk',
            name='explanation',
            field=models.TextField(blank=True, default=True),
        ),
    ]
