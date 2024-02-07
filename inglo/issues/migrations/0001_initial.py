# Generated by Django 4.2.6 on 2024-02-07 05:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField()),
                ('writer', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='IssueList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('views', models.IntegerField(default=0)),
                ('likes', models.IntegerField(default=0)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('country', models.IntegerField()),
                ('sdgs', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('issue', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='list', to='issues.issue')),
            ],
        ),
        migrations.CreateModel(
            name='IssueImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.URLField()),
                ('issue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='issues.issue')),
            ],
        ),
        migrations.CreateModel(
            name='IssueComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('issue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='issues.issue')),
                ('parent_comment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='issues.issuecomment')),
            ],
        ),
    ]
