# Generated by Django 4.2.6 on 2024-02-18 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_post_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
