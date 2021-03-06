# Generated by Django 3.0.5 on 2020-05-07 09:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('qmain', '0002_assignmentlinks_assignments_task_tasklinks'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='students',
            field=models.ManyToManyField(to='users.Student'),
        ),
        migrations.AlterField(
            model_name='course',
            name='lector',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Teacher'),
        ),
        migrations.AddField(
            model_name='tasklinks',
            name='task_file',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qmain.Task'),
        ),
        migrations.AddField(
            model_name='task',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qmain.Course'),
        ),
        migrations.AddField(
            model_name='assignmentlinks',
            name='task_file',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qmain.Assignments'),
        ),
    ]
