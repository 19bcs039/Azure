# Generated by Django 4.0.3 on 2023-04-06 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainAPP', '0005_match_is_test_match_match_match_pause_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='player_pic',
            field=models.TextField(blank=True, default='https://www.cricbuzz.com/a/img/v1/152x152/i1/c182026/rajat-patidar.jpg', null=True),
        ),
    ]