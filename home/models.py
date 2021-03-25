from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    task_title = models.CharField(max_length=30)
    task_description = models.TextField()
    complete = models.BooleanField(default=False)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task_title
    
class Meta:
    ordering = ['complete']
