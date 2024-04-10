from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Profile(models.Model):
    nick_name = models.OneToOneField(User, related_name='cur_user', on_delete=models.PROTECT)
    avatar = models.ImageField(null=True, blank=True)
    rate = models.IntegerField()
    registration_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

     # def __str__(self):
     #     return self.nick_name

class Tag(models.Model):

    tag_name = models.CharField(max_length=255, default="")

    def __str__(self):
        return self.tag_name

class Question(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)
    header = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    rate = models.IntegerField()
    img = models.ImageField(null=True, blank=True)
    creating_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.header

class Answer(models.Model):
    STATUS_CHOICES = [("l", "Legit"), ("nl", "Not legit")]
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.CharField()
    rate = models.IntegerField()
    status = models.CharField(choices=STATUS_CHOICES)
    creating_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content



class QuestionLike(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    question = models.ForeignKey(Question,related_name= 'question_likes', on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        unique_together = ("user", "question")


class AnswerLike(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, related_name= 'answer_likes',on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        unique_together = ("user", "answer")




