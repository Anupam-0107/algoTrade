# Generated by Django 4.0.3 on 2022-03-31 05:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0004_aliceblue_delete_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='aliceblue',
            name='aliceId',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='aliceblue',
            name='aliceblueId',
            field=models.CharField(max_length=50, verbose_name='AliceBlue id'),
        ),
    ]