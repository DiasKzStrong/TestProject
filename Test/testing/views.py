import json
from django.shortcuts import render,get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework.exceptions import NotFound
from rest_framework import generics
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from django.contrib.auth import authenticate,login,logout
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .models import *
from .serializers import *
from .paginators import *
from .permissions import *
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
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]
    
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
    permission_classes = [IsAdminUser]
    
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
    
class UserStatisticsMeView(generics.RetrieveUpdateAPIView):
    queryset = UserStatistics.objects.all()
    serializer_class = UserStatisticsSerializer
    permission_classes = [IsAuthenticated]
    def get_object(self):
        queryset = self.get_queryset()
        queryset = self.filter_queryset(queryset)
        
        return queryset.get(user=self.request.user)
    
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
    permission_classes = [IsAuthenticated]
    
    def get_object(self):
        queryset = self.get_queryset()
        object = get_object_or_404(queryset,user=self.request.user,test__id = self.kwargs['test__id'])
        return object
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response('Object succesfully deleted',status=status.HTTP_204_NO_CONTENT)

class CommentsView(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_superuser:
            return super().get_queryset()
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)

    def get_object(self):
        instance = super().get_object()
        if instance.user == self.request.user:
            return instance
        else:
            self.permission_classes = [NotFoundBlock]
            raise NotFound('Forbidden, not your comment')
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response('Object succesfully deleted',status=status.HTTP_204_NO_CONTENT)
