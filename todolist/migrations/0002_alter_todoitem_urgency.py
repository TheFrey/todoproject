# Generated by Django 4.1.1 on 2022-09-20 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='urgency',
            field=models.CharField(choices=[('white', 'None'), ('red', 'Срочно'), ('aliceblue', 'Необходимо'), ('green', 'Не срочно')], default='white', max_length=10),
        ),
    ]