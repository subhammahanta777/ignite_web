from django.db import models

# Create your models here.

class question_bank(models.Model):
    question = models.FileField()
    answer = models.CharField(max_length=2000)
    is_correct = models.IntegerField()
    visited= models.BooleanField(default= False)
    def __str__(self):
        return str(self.id)

class hint(models.Model):
    question_id= models.ForeignKey(question_bank , on_delete= models.CASCADE)
    hint1 = models.CharField(max_length=1000)
    hint2 = models.CharField(max_length=1000)
    hint3 = models.CharField(max_length=1000)
    hint4 = models.CharField(max_length=1000)
    def __str__(self):
        return str(self.question_id)