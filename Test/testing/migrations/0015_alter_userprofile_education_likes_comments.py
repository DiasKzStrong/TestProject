# Generated by Django 4.1.7 on 2023-03-16 16:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0014_test_create_at_test_views_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='education',
            field=models.CharField(choices=[('HighShool', 'Highshool'), ('University', 'University'), ('Employee', 'Employee')], default=None, max_length=255, null=True),
        ),
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='test_likes', to='testing.test')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_likes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='test_comments', to='testing.test')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_comments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
