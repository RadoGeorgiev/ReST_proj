from django.db import models

# Create your models here.


class Question(models.Model):
    author = models.CharField(max_length=200, default="Anonymous")
    question = models.TextField()

    def __str__(self):
        return f"{self.author}: {self.question}"


'''
this
 is 
 a
 placeholder
   for 
   documentation 
   or longer comments
'''


class Answer(models.Model):
    author = models.CharField(max_length=200, default="Anonymous")
    content = models.TextField()
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)
    question_key = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.author} {self.content[:10]}...'


