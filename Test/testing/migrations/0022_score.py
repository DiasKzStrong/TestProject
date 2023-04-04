# Generated by Django 4.1.7 on 2023-03-29 14:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0021_alter_answer_unique_together'),
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.FloatField()),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='score_test', to='testing.test')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='score_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
