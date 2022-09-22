from django.db import models
from django.contrib.auth.models import User



class ToDoItem(models.Model):

    def modify_url(self):
        return '/modify/{}/'.format(self.id)

    def add_sub_item_url(self):
        return '/{}/{}/'.format(self.id, self.date)

    def del_item_url(self):
        return '/delete/{}/'.format(self.id)

    STATUS_CHOICES = (
        ('white', 'None'),
        ('red', 'Срочно'),
        ('darkorange', 'Необходимо'),
        ('green', 'Не срочно')
    )

    user = models.ForeignKey(User, related_name='todo_item', on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    urgency = models.CharField(max_length=10, choices=STATUS_CHOICES, default='white')
    date = models.DateField(auto_now_add=True)


class SubItem(models.Model):
    item = models.ForeignKey(ToDoItem, related_name='sub_item', on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    date = models.DateField(auto_now_add=True)
