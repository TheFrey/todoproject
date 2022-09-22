# Generated by Django 4.1.1 on 2022-09-20 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0003_alter_todoitem_urgency'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=300)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_item', to='todolist.todoitem')),
            ],
        ),
    ]