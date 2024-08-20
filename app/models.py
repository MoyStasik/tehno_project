from django.contrib.auth.models import User
from django.db import models

# Create your models here.
def answers_count(question_id):
    return Answer.objects.filter(question=question_id).count()

def tag_exist(name):
    tag_list = Tag.objects.filter(tag_name = name)
    if len(tag_list) == 0:
        return False
    return True

def tag_by_tag_name(name):
    return Tag.objects.get(tag_name=name)

def profile_by_user(user):
    return Profile.objects.get(nick_name=user)

def question_by_id(number):
    return Question.objects.get(id = number)

def answers_by_question_id(number):
    return Answer.objects.filter(question = number)

def new_questions():
    question_list = Question.objects.order_by('-creating_date')
    return question_list

def hot_100_question():
    question_list = Question.objects.order_by('-rate')[:100]
    return question_list

def question_by_tag(name):
    one_tag = Tag.objects.get(tag_name = name)
    question_list = Question.objects.filter(tag = one_tag.id)
    return question_list

class Profile(models.Model):
    nick_name = models.OneToOneField(User, related_name='cur_user', on_delete=models.PROTECT)
    name = models.CharField(max_length=255, default="")
    avatar = models.ImageField(upload_to="img")
    rate = models.IntegerField()
    registration_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)


class Tag(models.Model):
    id = models.AutoField(auto_created=True,primary_key=True, unique=True)
    tag_name = models.CharField(max_length=255)

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
    # def set_rate(self):


class Answer(models.Model):
    STATUS_CHOICES = [("l", "Legit"), ("nl", "Not legit")]
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.CharField()
    rate = models.IntegerField()
    status = models.CharField(choices=STATUS_CHOICES)
    creating_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)





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




