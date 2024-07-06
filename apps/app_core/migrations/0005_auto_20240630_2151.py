# Generated by Django 3.2.23 on 2024-06-30 13:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_core', '0004_collection_imgurl'),
    ]

    operations = [
        migrations.AddField(
            model_name='folder',
            name='is_invisible',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='invisible_folder',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='invisible_profile', to='app_core.folder'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='folderId',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_core.folder'),
        ),
    ]