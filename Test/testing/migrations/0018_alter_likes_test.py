# Generated by Django 4.1.7 on 2023-03-18 15:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0017_alter_test_title_alter_userstatistics_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likes',
            name='test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='test_likes', to='testing.test'),
        ),
    ]
