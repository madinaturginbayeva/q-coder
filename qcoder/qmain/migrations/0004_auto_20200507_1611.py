# Generated by Django 3.0.5 on 2020-05-07 10:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('qmain', '0003_auto_20200507_1545'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignments',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Student'),
        ),
        migrations.AddField(
            model_name='assignments',
            name='task',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='qmain.Task'),
        ),
    ]
