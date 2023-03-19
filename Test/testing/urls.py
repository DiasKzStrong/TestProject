from django.urls import path,include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'tests',TestSingleView,basename='testsingle')
router.register(r'likes',LikesView,basename='likes')
router.register(r'comments',CommentsView,basename='comment')


app_name = 'api'
urlpatterns = [
    
    path('tests',TestView.as_view(),name='tests'),
    path('category',CategoryView.as_view(),name='category'),
    path('category/<str:name>',CategorySingleView.as_view(),name='categorysingle'),
    path('questions',QuestionsView.as_view(),name='questions'),
    path('users',UserView.as_view(),name='users'),
    path('users/me',UserMeView.as_view(),name='me'),
    path('users/<str:username>',UserSingleView.as_view(),name='usersingle'),
    path('userstats',UserStatisticsView.as_view(),name='userstats'),
    path('userstats/<str:user__username>',UserStatisticsSingleView.as_view(),name='userstatssingle'),
    path('user/stats/me',UserStatisticsMeView.as_view(),name='userstatsme'),
    path('userprofile/<str:user_username>',UserProfileSingleView.as_view(),name='user-profile'),
    path('user/profile/me',UserProfileMeView.as_view(),name='userprofileme'),
    path('login',user_login,name='login'),
    path('logout',user_logout,name='logout'),
    path('register',UserRegistrationView.as_view(),name='register'),
    
    #viewsets 
    path('',include(router.urls)),
    
]