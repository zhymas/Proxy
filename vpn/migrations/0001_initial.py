# Generated by Django 4.1.7 on 2023-11-14 00:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProxyURLObj',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin_url', models.URLField()),
                ('user_request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='proxy_requests', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
