# Generated by Django 4.2.6 on 2024-02-14 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0002_alter_issue_image_url_alter_issue_writer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='writer',
            field=models.CharField(blank=True, default='unknown', max_length=100, null=True),
        ),
    ]
