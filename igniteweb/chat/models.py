from django.db import models

# Create your models here.

class user_chat_logs(models.Model):
    user_id=models.IntegerField()
    text_sent = models.CharField(max_length=2000)
    text_recieved = models.CharField(max_length=2000)
    time_stamp= models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.id)
