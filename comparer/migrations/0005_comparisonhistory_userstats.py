# Generated by Django 5.1.3 on 2024-11-16 17:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comparer', '0004_scheduledtask_user_alter_scheduledtask_next_run'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ComparisonHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file1', models.CharField(max_length=255)),
                ('file2', models.CharField(max_length=255)),
                ('comparison_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('completed', 'Completed'), ('failed', 'Failed'), ('in_progress', 'In Progress')], max_length=20)),
                ('differences_found', models.IntegerField(default=0)),
                ('execution_time', models.FloatField(help_text='Execution time in seconds')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-comparison_date'],
            },
        ),
        migrations.CreateModel(
            name='UserStats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_comparisons', models.IntegerField(default=0)),
                ('total_time_saved', models.FloatField(default=0, help_text='Time saved in hours')),
                ('subscription_type', models.CharField(choices=[('free', 'Free'), ('premium', 'Premium'), ('enterprise', 'Enterprise')], default='Free', max_length=20)),
                ('comparisons_limit', models.IntegerField(default=100)),
                ('comparisons_used', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
