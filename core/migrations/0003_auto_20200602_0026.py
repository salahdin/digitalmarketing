# Generated by Django 3.0.6 on 2020-06-01 22:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0002_auto_20200602_0017'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uploadDate', models.DateTimeField(auto_created=True, default=django.utils.timezone.now, verbose_name='date and time of upload')),
                ('Service_name', models.CharField(max_length=50, verbose_name='product/service name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='service/product description')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='seller', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Assessment',
        ),
    ]