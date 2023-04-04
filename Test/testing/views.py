from django.shortcuts import render,get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.exceptions import NotFound
from rest_framework import generics
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import *
from django.contrib.auth import authenticate,login,logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import check_password
from .models import *
from .serializers import *
from .paginators import *
from .permissions import *

from django.core.mail import EmailMessage
from django.contrib.auth.tokens import PasswordResetTokenGenerator,default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.utils.http import urlsafe_base64_decode

# Create your views here.

# Classes for all objects

#User views
@csrf_exempt
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            user_obj = UserSerializer(user).data
            return JsonResponse({'user':user_obj})
        return JsonResponse({'message':'Error login'})
    return JsonResponse({'message':'You should send POST request'})


def user_logout(request):
    logout(request)
    return JsonResponse({'message':'Succesfully logout'})


class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer


class UserProfileSingleView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    lookup_field = 'user_username'
    permission_classes = [IsAdminUser]
    
    def get_object(self):
        self.permission_classes = []
        queryset = self.get_queryset()
        queryset = self.filter_queryset(queryset)
        try:
            return_queryset = queryset.get(user__username = self.kwargs['user_username'])
        except ObjectDoesNotExist:
            self.permission_classes = [NotFoundBlock]
            raise NotFound('object does not exists')
        return return_queryset
    
class UserProfileMeView(generics.RetrieveUpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        queryset = self.get_queryset()
        queryset = self.filter_queryset(queryset)
        instance = queryset.get(user=self.request.user)
        return instance
    
class UserView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [OnlyAdminPost]
    
    def get_queryset(self):
        queryset = super().get_queryset()
        if 'username' in self.request.query_params:
            queryset = queryset.filter(username=self.request.query_params['username'])
        return queryset
    
class UserMeView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    
    def get_object(self):
        queryset = self.get_queryset()
        queryset = self.filter_queryset(queryset)
        
        return queryset.get(username=self.request.user.username)
    
class UserSingleView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'
    permission_classes = [OnlyAdminPost]
    
class UserStatisticsView(generics.ListCreateAPIView):
    queryset = UserStatistics.objects.all()
    serializer_class = UserStatisticsSerializer
    permission_classes = [IsAdminUser] 
    

class UserStatisticsSingleView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserStatistics.objects.all()
    serializer_class = UserStatisticsSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'user__username'
    
    def get_object(self):
        self.permission_classes = []
        queryset = self.get_queryset()
        queryset = self.filter_queryset(queryset)
        try:
            return_queryset = queryset.get(user__username = str(self.kwargs['user__username']))
        except ObjectDoesNotExist:
            self.permission_classes = [NotFoundBlock]
            raise NotFound('object does not exists')
        return return_queryset
    
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        objects_to_add = request.data.get('done_tests', [])
        for obj_id in objects_to_add:
            obj = Test.objects.get(id=obj_id)
            instance.done_tests.add(obj)

        instance.save()

        serializer = self.get_serializer(instance)
        return Response(serializer.data)
    
    
    
class UserStatisticsMeView(generics.RetrieveUpdateAPIView):
    queryset = UserStatistics.objects.all()
    serializer_class = UserStatisticsSerializer
    permission_classes = [IsAuthenticated]
    def get_object(self):
        queryset = self.get_queryset()
        queryset = self.filter_queryset(queryset)
        try:
            instance = queryset.get(user=self.request.user)
        except ObjectDoesNotExist:
            UserStatistics.objects.create(user=self.request.user)
            instance = queryset.get(user=self.request.user)
        return instance

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        objects_to_add = request.data.get('done_tests', [])
        for obj_id in objects_to_add:
            obj = Test.objects.get(id=obj_id)
            instance.done_tests.add(obj)

        instance.save()

        serializer = self.get_serializer(instance)
        return Response(serializer.data)
    
    
    
#other views 

class TestView(generics.ListCreateAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    permission_classes = [OnlyAdminPost]
    
    
class CategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [OnlyAdminPost]
    
class CategorySingleView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'name'
    permission_classes = [OnlyAdminPost]
    
class QuestionsView(generics.ListCreateAPIView):
    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializer
    filter_backends = [OrderingFilter]
    ordering_fields = ['test']
    permission_classes = [OnlyAdminPost]
    
    def get_queryset(self):
        queryset = super().get_queryset()
        if 'test' in self.request.query_params:
            queryset = queryset.filter(test__title=self.request.query_params['test'])
        return queryset
    
class AnswerView(generics.ListCreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
        

# Classes for single objects
class TestSingleView(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    lookup_field = 'id'
    permission_classes = [OnlyAdminPost]
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializers = self.get_serializer(instance)
        return Response(serializers.data,status=status.HTTP_200_OK)
    
class LikesView(viewsets.ModelViewSet):
    queryset = Likes.objects.all()
    serializer_class = LikesSerializer
    lookup_field = 'test__id'
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get_queryset(self):
        return super().get_queryset()
    
    def get_object(self):
        if self.request.user.is_authenticated:          
            queryset = self.get_queryset()
            object = get_object_or_404(queryset,user=self.request.user,test__id = self.kwargs['test__id'])
            return object
        raise NotFound('authentication credentials were not provided')
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response('Object succesfully deleted',status=status.HTTP_204_NO_CONTENT)

class CommentsView(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self):
        instance = super().get_object()
        if instance.user == self.request.user or self.request.user.is_superuser:
            return instance
        else:
            self.permission_classes = [NotFoundBlock]
            raise NotFound('Forbidden, not your comment')
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response('Object succesfully deleted',status=status.HTTP_204_NO_CONTENT)


class ScoreView(generics.ListCreateAPIView):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer
    permission_classes = [IsAuthenticated]

class ScoreInlineView(generics.RetrieveUpdateAPIView):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = ('test_id','user_id')
    def get_object(self):
        queryset = self.get_queryset()
        queryset = self.filter_queryset(queryset)
        print(self.kwargs)
        obj = queryset.get(test=self.kwargs[self.lookup_field[0]], user=self.request.user)
        
        return obj
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        score = float(request.data['score'])
        if score > instance.score:
            instance.score = score
            instance.save()
        else:
            return Response({'error':'score must be higher than current score'})
        return Response(ScoreSerializer(instance).data,status=status.HTTP_202_ACCEPTED)
    
    
# Парольдын темасы 

class PasswordUpdateView(APIView):
    
    @csrf_exempt
    def post(self, request):
        serializer = PasswordUpdateSerializer(data=request.data)
        if serializer.is_valid():
            user = request.user
            current_password = serializer.data.get('current_password')
            new_password = serializer.data.get('new_password')
            if check_password(current_password, user.password):
                user.set_password(new_password)
                user.save()
                return Response({'message':'password changed'},status=status.HTTP_200_OK)
            else:
                return Response({'current_password': ['Incorrect password.']}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        

class PasswordResetRequestView(APIView):
    def post(self, request):
        serializer = PasswordResetRequestSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.data.get('email')
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                return Response({'email': ['User with this email does not exist.']}, status=status.HTTP_400_BAD_REQUEST)
            token_generator = PasswordResetTokenGenerator()
            token = token_generator.make_token(user)
            uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
            reset_link = f"{request.scheme}://{request.get_host()}/reset-password/{uidb64}/{token}"
            email = EmailMessage(
                'Password reset link',
                f'Use the following link to reset your password: {reset_link}',
                to=[email]
                
            )
            email.content_subtype = 'html'
            email.send()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PasswordResetView(APIView):
    def post(self, request, uidb64, token):
        serializer = PasswordResetSerializer(data=request.data)
        if serializer.is_valid():
            try:
                uid = urlsafe_base64_decode(uidb64).decode('utf-8')
                user = User.objects.get(pk=uid)
            except (TypeError, ValueError, OverflowError, User.DoesNotExist):
                user = None
            if user is not None and PasswordResetTokenGenerator().check_token(user, token):
                new_password = serializer.data.get('new_password')
                user.set_password(new_password)
                user.save()
                return Response(status=status.HTTP_200_OK)
            else:
                return Response({'token': ['Invalid token.']}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




# email reset

class EmailRequestView(APIView):
    def post(self, request):
        serializer = PasswordResetSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.data.get('email')
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                return Response({'detail': 'User with this email does not exist.'}, status=status.HTTP_404_NOT_FOUND)
            token_generator = default_token_generator
            token = token_generator.make_token(user)    
            reset_url = f'{request.scheme}://{request.get_host()}/reset-password/{user.pk}/{token}/'
            email = EmailMessage(
                'Reset email',
                reset_url,
                to=[email]
                
            )
            email.content_subtype = 'html'
            email.send()
            return Response({'detail': 'Email reset email has been sent.'}, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'Email is required.'}, status=status.HTTP_400_BAD_REQUEST)


class EmailResetView(APIView):
    def put(self,request,pk,token):
        serializer = PasswordResetSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.data.get('email')
            try:
                user = User.objects.get(pk=pk)
            except User.DoesNotExist:
                return Response({"message":"User does not exist"},status=status.HTTP_404_NOT_FOUND)
            if User.objects.filter(email=email).exists():
                return Response({"message":"that email already taken"})
            if user and PasswordResetTokenGenerator().check_token(user,token):
                user.email = email
                user.save()
                return Response(status=status.HTTP_202_ACCEPTED)
            else:
                return Response({"message":"not valid token"},status=status.HTTP_403_FORBIDDEN)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        

# Just views 



def add_view(request,pk):
    test = get_object_or_404(Test, id=pk)
    views = ViewsCount.objects.get(test=test)
    views.views = views.views+1
    views.save()
    return JsonResponse({'message':'succesfully added'})