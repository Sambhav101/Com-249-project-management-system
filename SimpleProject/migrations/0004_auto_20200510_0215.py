# Generated by Django 3.0.6 on 2020-05-10 06:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('SimpleProject', '0003_task_groups_copy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='groups_copy',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='auth.Group'),
        ),
    ]
