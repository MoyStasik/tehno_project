import random

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError
from app.models import Profile, Tag, Question, Answer, QuestionLike, AnswerLike
from faker import Faker


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument("ratio", nargs="?", type=int, default = 15)

    def handle(self, *args, **options):
        # fill users and profiles
        # profiles = set()
        users = set()
        fake = Faker()



        # questions = Question.objects.all()
        # answers = Answer.objects.all()
        # for q in questions:
        #     q.rate = 0
        #     q.rate = len(QuestionLike.objects.all().filter(question = q.id))
        #     q.save()
        #
        # for a in answers:
        #     a.rate = 0
        #     a.rate = len(AnswerLike.objects.all().filter(answer = a.id))
        #     a.save()

        # for i in range(options["ratio"]):
        #     _name = fake.unique.name()
        #     #rating = fake.random.randint(10, 1000)
        #     _email = fake.unique.email()
        #     _password = fake.unique.password()
        #     us = User.objects.create_user(
        #         username = _name,
        #         email = _email,
        #         password = _password,
        #     )
            # prof = Profile.objects.create(
            #     nick_name = us,
            #     rate=rating
            # )
            # profiles.add(prof)
            # users.add(us)
        # User.objects.bulk_create(users)
        # user_list = User.objects.all()
        # profiles = [Profile(nick_name=user, name=user.username, rate = fake.random.randint(10, 1000))
        #             for user in user_list]
        # Profile.objects.bulk_create(profiles)


        # then fill tags
        # tags = set()
        # for i in range(options["ratio"]):
        #     tag_value = fake.unique.text()[:random.randint(3, 8)]
        #     tg = Tag.objects.create(
        #         tag_name = tag_value
        #     )
        #     tags.add(tg)
        # Tag.objects.bulk_create(tags)

        # #then fill questions
        # # user = models.ForeignKey(Profile, on_delete=models.CASCADE)
        # # tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
        # # header = models.CharField(max_length=255)
        # # content = models.CharField(max_length=255)
        # # rate = models.IntegerField()
        #


        # Question.objects.all().delete()
        # questions = set()
        # for i in range(options["ratio"] * 10):
        #     _header = fake.sentence() + "?"
        #     _content = fake.text()
        #     rating = fake.random.randint(100, 1000)
        #     question = Question.objects.create(
        #         user = random.choice(Profile.objects.all()),
        #         header = _header,
        #         content = _content,
        #         rate = rating
        #     )
        # tag_objects = Tag.objects.all()
        # questions = Question.objects.all()
        # for q in questions:
        #     for _ in range(random.randint(2, 7)):
        #         q.tag.add(random.choice(tag_objects))


        #     questions.add(question)
        # Question.objects.bulk_create(questions)


        # # then fill answer
        # # class Answer(models.Model):
        # #     user = models.ForeignKey(Profile, on_delete=models.CASCADE)
        # #     question = models.ForeignKey(Question, on_delete=models.CASCADE)
        # #     content = models.CharField()
        # #     rate = models.IntegerField()
        # #     status = models.BooleanField()
        # #     creating_date = models.DateTimeField(auto_now_add=True)
        # #     updated_at = models.DateTimeField(auto_now=True)
        #
        # answers = set()
        # for i in range(options["ratio"] * 100):
        #     _content = fake.text()
        #     rating = fake.random.randint(100, 1000)
        #
        #     answer = Answer.objects.create(
        #         status = random.choice(Answer.STATUS_CHOICES),
        #         user = random.choice(Profile.objects.all()),
        #         question = random.choice(Question.objects.all()),
        #         content = _content,
        #         rate = rating
        #     )
        #     answers.add(answer)
        # Answer.objects.bulk_create(answers)
        #
        # # class QuestionLike(models.Model):
        # #     user = models.ForeignKey(Profile, on_delete=models.CASCADE)
        # #     question = models.ForeignKey(Question, related_name='question_likes', on_delete=models.CASCADE)
        # #     updated_at = models.DateTimeField(auto_now=True)
        # #
        # #     class Meta:
        # #         unique_together = ("user", "question")
        # #then fill likes
        # likes1 = set()
        # for i in range(options["ratio"] * 100):
        #     quest = random.choice(Question.objects.all())
        #     like = QuestionLike.objects.create(
        #         user = random.choice(Profile.objects.all()),
        #         question = quest
        #     )
        #     likes1.add(like)
        # QuestionLike.objects.bulk_create(likes1)

        # then fill likes
        # likes2 = set()
        # for i in range(options["ratio"] * 100):
        #     like = AnswerLike.objects.create(
        #         user=random.choice(Profile.objects.all()),
        #         answer=random.choice(Answer.objects.all())
        #     )
        #     likes2.add(like)
        # AnswerLike.objects.bulk_create(likes2)