# Generated by Django 2.2.8 on 2020-07-03 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20200703_1042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='postImage',
            field=models.ImageField(null=True, upload_to='avatar/'),
        ),
    ]
