# Generated by Django 4.1.7 on 2023-04-02 05:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0025_remove_test_views_count'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='viewscount',
            unique_together={('test', 'views')},
        ),
    ]