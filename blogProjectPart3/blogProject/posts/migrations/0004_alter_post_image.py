# Generated by Django 5.1.3 on 2024-12-29 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='posts/media/uploads/'),
        ),
    ]
