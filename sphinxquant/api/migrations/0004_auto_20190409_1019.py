# Generated by Django 2.1.7 on 2019-04-09 10:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20190409_0922'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='backtest',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterModelOptions(
            name='strategy',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterModelOptions(
            name='strategycode',
            options={'ordering': ['-created_at']},
        ),
    ]
