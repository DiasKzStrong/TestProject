from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from .models import *

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'
        
class QuestionsSerializer(serializers.ModelSerializer):
    answer = AnswerSerializer(source='answers',many=True)
    class Meta:
        model = Questions
        fields = ('id','test','question_text','answer')
    
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['test'] = instance.test.title
        return rep

class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = ('user','test','score')
        
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['test'] = instance.test.title
        rep['user'] = instance.user.username
        return rep
    
class TestInlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ('id','title','create_at')
        

class LikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Likes
        fields = '__all__'
        
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['test'] = instance.test.title, instance.test.id
        rep['user'] = instance.user.username
        return rep
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['test'] = instance.test.title, instance.test.id
        rep['user'] = instance.user.username
        return rep
    
class ViewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ViewsCount
        field = 'views'
        exclude = ('test','id')

class TestSerializer(serializers.ModelSerializer):
    likes = LikesSerializer(many=True,source='test_likes',read_only=True)
    comments = CommentSerializer(many=True,source='test_comments',read_only=True)
    questionss = QuestionsSerializer(many=True,source='questions',read_only=True)
    views = ViewsSerializer(many=True,source='viewtest',read_only=True)
    class Meta:
        model = Test
        fields = ('id','title','category','create_at','views','likes','comments','questionss')
    
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['category'] = instance.category.name
        rep['views'] = ":".join([str(view['views']) for view in rep['views']])
        return rep
        
    def create(self, validated_data):
        test = Test.objects.create(**validated_data)
        test.save()
        views = ViewsCount.objects.create(test=test,views=0)
        views.save()
        return test
class CategorySerializer(serializers.ModelSerializer):
    test = TestInlineSerializer(many=True,source = 'test_set',read_only = True)
    class Meta:
        model = Category
        fields = ('id','name','test')
          
          
class UserStatisticsSerializer(serializers.ModelSerializer):
    done_tests = serializers.SerializerMethodField()

    class Meta:
        model = UserStatistics
        fields = ['user','done_tests']

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['user'] = instance.user.username
        # rep['score'] = instance.done_tests.score
        return rep
    
    def get_done_tests(self, obj):
        user = obj.user
        done_tests = obj.done_tests.all()
        serialized_tests = []
        
        for test in done_tests:
            scores = Score.objects.filter(test=test, user=user)
            serialized_scores = ScoreSerializer(scores, many=True).data
            if serialized_scores:
                serialized_score = serialized_scores[0]['score']
            else:
                serialized_score = None
            serialized_test = TestInlineSerializer(test).data
            serialized_test['score'] = serialized_score
            serialized_tests.append(serialized_test)
            
        return serialized_tests


    # def create(self, validated_data):
    #     score = validated_data.pop('score')
        
        
class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','email','password')
        extra_kwargs = {'password':{'write_only':True,'style':{'input_type': 'password'}}}
        
    def create(self, validated_data):
        password = validated_data.pop('password')
        email = validated_data['email']
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'error':'that email already user by other user'})
        user = User.objects.create(username=validated_data['username'],email=validated_data['email'])
        user.set_password(password)
        user.save()
        UserProfile.objects.create(user=user,city=None)
        UserStatistics.objects.create(user=user)
        return user
    
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'
        
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['user'] = instance.user.username
        return rep


class UserSerializer(serializers.ModelSerializer):
    likes = LikesSerializer(source='user_likes',many=True,read_only=True)
    user_profile = UserProfileSerializer(source='profile',many=True)
    user_statistic = UserStatisticsSerializer(source='statistic',many=True)
    class Meta:
        model = User
        field= ['__all__','user_profile','user_statistic','likes']
        exclude = ['password','is_superuser','groups','user_permissions','is_staff','is_active']

class CustomUserSerializer(UserSerializer):
    class Meta:
        model = User
        exclude = ['password']
    
    def to_representation(self, instance):
        user = self.context['request'].user
        if user.is_superuser:
            return super().to_representation(instance)
        return UserSerializer(instance, context=self.context).data
    


# Пароль сериалайзер


class PasswordUpdateSerializer(serializers.Serializer):
    current_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    
class PasswordResetRequestSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    
class PasswordResetSerializer(serializers.Serializer):
    new_password = serializers.CharField(required=True)