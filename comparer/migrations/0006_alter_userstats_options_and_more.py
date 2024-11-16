# Generated by Django 5.1.3 on 2024-11-16 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comparer', '0005_comparisonhistory_userstats'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userstats',
            options={'verbose_name': 'User Statistics', 'verbose_name_plural': 'User Statistics'},
        ),
        migrations.RenameField(
            model_name='userstats',
            old_name='comparisons_used',
            new_name='comparisons_this_month',
        ),
        migrations.RemoveField(
            model_name='userstats',
            name='comparisons_limit',
        ),
        migrations.AddField(
            model_name='userstats',
            name='last_comparison_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userstats',
            name='subscription_type',
            field=models.CharField(default='Free', max_length=50),
        ),
    ]