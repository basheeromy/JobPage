# Generated by Django 4.2.6 on 2023-10-23 17:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_user_is_active_user_is_staff'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resume', models.FileField(null=True, upload_to='')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='userprofile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
