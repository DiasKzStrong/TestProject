# Generated by Django 4.0.2 on 2023-03-16 02:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0012_alter_userprofile_user_alter_userstatistics_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='test',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='test_question', to='testing.test', to_field='title'),
        ),
    ]
