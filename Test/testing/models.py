from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    
    def __str__(self) -> str:
        return self.username
    
    class Meta:
        unique_together = ['email','username']

class Category(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return f'{self.name}'
    
    class Meta:
        unique_together = ['name']
        
class Test(models.Model):
    title = models.CharField(max_length=255,unique=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = ['title']
        
    def __str__(self) -> str:
        return self.title
    
class ViewsCount(models.Model):
    test = models.ForeignKey(Test,on_delete=models.CASCADE,related_name='viewtest')
    views = models.IntegerField()
        
    class Meta:
        unique_together = ('test','views')
    
class Questions(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='questions',db_constraint=True,to_field='title')
    question_text = models.TextField(unique=True)

    def __str__(self):
        return self.question_text


class Answer(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE, related_name='answers',to_field='question_text')
    answer_text = models.TextField()
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.answer_text
    
    class Meta:
        unique_together = ['question', 'answer_text']

class UserStatistics(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='statistic',db_constraint=True,to_field='username')
    done_tests = models.ManyToManyField(Test,related_name='done_tests')
    

class UserProfile(models.Model):
    choices_sex = (('Man','M'),('Women','W'))
    choices_education = (('HighShool','Highshool'),('University','University'),('Employee','Employee'))
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='profile',to_field='username',db_constraint=True)
    city = models.CharField(max_length=255,default=None,null=True)
    sex = models.CharField(max_length=255,choices=choices_sex,default=None,null=True)
    education = models.CharField(max_length=255,choices=choices_education,default=None,null=True)
    
    class Meta:
        unique_together = ['user']
         
class Likes(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_likes')
    test = models.ForeignKey(Test,on_delete=models.CASCADE,related_name='test_likes')
    
    class Meta:
        unique_together = ('test', 'user',)
    
class Comments(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_comments')
    test = models.ForeignKey(Test,on_delete=models.CASCADE,related_name='test_comments')
    comment = models.TextField()
    
class Score(models.Model):
    test = models.ForeignKey(Test,on_delete=models.CASCADE,related_name='score_test')
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='score_user')
    score = models.IntegerField()
    
    class Meta:
        unique_together = ('test','user')