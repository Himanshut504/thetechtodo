# Generated by Django 3.0.2 on 2020-02-19 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_remove_task_dates'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='complete',
            field=models.CharField(choices=[('3', 'Choose any...'), ('2', 'Completed'), ('1', 'Prioritize')], default='1', max_length=6000),
        ),
    ]
