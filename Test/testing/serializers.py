from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from rest_framework.response import Response
from rest_framework import status
from .models import *

class QuestionsSerializer(serializers.ModelSerializer):
    
    def validate(self, attrs):
        if attrs['right'] == attrs['other1'] or attrs['right'] == attrs['other2'] or attrs['right'] == attrs['other3']:
            raise serializers.ValidationError('Бірдей болмау керек')
        elif attrs['other1'] == attrs['right'] or attrs['other1'] == attrs['other2'] or attrs['other1'] == attrs['other3']:
            raise serializers.ValidationError('Бірдей болмау керек')
        elif attrs['other2'] == attrs['other1'] or attrs['other2'] == attrs['right'] or attrs['other2'] == attrs['other3']:
            raise serializers.ValidationError('Бірдей болмау керек')
        elif attrs['other3'] == attrs['other1'] or attrs['other3'] == attrs['right'] or attrs['other2'] == attrs['other3']:
            raise serializers.ValidationError('Бірдей болмау керек')
        return attrs
    
    class Meta:
        model = Questions
        fields = '__all__'
    
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['test'] = instance.test.title
        return rep

        
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

class TestSerializer(serializers.ModelSerializer):
    likes = LikesSerializer(many=True,source='test_likes',read_only=True)
    comments = CommentSerializer(many=True,source='test_comments',read_only=True)
    questions = QuestionsSerializer(many=True,source='test_question',read_only=True)
    class Meta:
        model = Test
        fields = ('id','title','category','create_at','views_count','likes','comments','questions')
    
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['category'] = instance.category.name
        return rep
        

class TestInlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ('id','title','create_at','views_count')

class CategorySerializer(serializers.ModelSerializer):
    test = TestInlineSerializer(many=True,source = 'test_set',read_only = True)
    class Meta:
        model = Category
        fields = ('id','name','test')
          
          
class UserStatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserStatistics
        fields = ['user','done_tests']
          
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['user'] = instance.user.username
        rep['done_tests'] = TestInlineSerializer(instance.done_tests.all(),many=True).data
        return rep

class UserRegistrationSerializer(serializers.ModelSerializer):
    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError('Password and confirm_password should be same')
        return attrs
    
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
        
        
class UserSerializer(serializers.ModelSerializer):
    user_profile = UserProfileSerializer(source='profile',many=True)
    user_statistic = UserStatisticsSerializer(source='statistic',many=True)
    class Meta:
        model = User
        field= ['__all__','user_profile','user_statistic']
        exclude = ['password']
