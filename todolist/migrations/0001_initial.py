# Generated by Django 4.1.1 on 2022-09-20 11:06

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
            name='ToDoItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=300)),
                ('urgency', models.CharField(choices=[('white', 'None'), ('red', 'Срочно'), ('blue', 'Необходимо'), ('green', 'Не срочно')], default='white', max_length=10)),
                ('date', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='todo_item', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
