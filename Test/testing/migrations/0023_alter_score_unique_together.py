# Generated by Django 4.1.7 on 2023-03-29 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0022_score'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='score',
            unique_together={('test', 'user')},
        ),
    ]
