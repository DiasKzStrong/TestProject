# Generated by Django 4.1.7 on 2023-03-11 07:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0003_alter_category_unique_together_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='test',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='testing.test'),
        ),
        migrations.AlterUniqueTogether(
            name='category',
            unique_together={('name',)},
        ),
        migrations.AlterUniqueTogether(
            name='test',
            unique_together={('title',)},
        ),
    ]