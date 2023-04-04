from django.urls import path,include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'tests',TestSingleView,basename='testsingle')
router.register(r'likes',LikesView,basename='likes')
router.register(r'comments',CommentsView,basename='comment')


app_name = 'api'
urlpatterns = [
    
    path('tests',TestView.as_view(),name='tests'), #Тесттар 
    path('category',CategoryView.as_view(),name='category'),# Категориялар
    path('category/<str:name>',CategorySingleView.as_view(),name='categorysingle'), # Категорияларга ид аркылы киресин
    path('questions',QuestionsView.as_view(),name='questions'),# каждый сурак
    path('score',ScoreView.as_view(),name='score'),
    path('test/<int:test_id>/score',ScoreInlineView.as_view(),name='scoreinline'),
    path('answer',AnswerView.as_view(),name='answer'),
    path('users',UserView.as_view(),name='users'),# Букил юзерлар
    path('users/me',UserMeView.as_view(),name='me'),# Аккаунтка кирген адамның информациясы
    path('users/<str:username>',UserSingleView.as_view(),name='usersingle'),# Каждый юзерге аты бойынша киресин
    path('userstats',UserStatisticsView.as_view(),name='userstats'),# Юзерлардың статистикасы
    path('userstats/<str:user__username>',UserStatisticsSingleView.as_view(),name='userstatssingle'),# юзер статистакасына аты бойынша киресин
    path('user/stats/me',UserStatisticsMeView.as_view(),name='userstatsme'),# нау кирген юзердың статистикасы
    path('userprofile/<str:user_username>',UserProfileSingleView.as_view(),name='user-profile'),# нау адамның типо профильы
    path('user/profile/me',UserProfileMeView.as_view(),name='userprofileme'),# кирген адамның профильы
    path('login',user_login,name='login'),# логин 
    path('logout',user_logout,name='logout'),# шыгу 
    path('register',UserRegistrationView.as_view(),name='register'),# регистрациясы
    
    #viewsets 
    path('',include(router.urls)),# на жерде тесттар и лайктар и комментар
    
    #Парольские темы
    path('password-update', PasswordUpdateView.as_view()),
    path('reset-password/request/', PasswordResetRequestView.as_view()),
    path('reset-password/<str:uidb64>/<str:token>/', PasswordResetView.as_view()),
    
    
    #email тема
    path('reset-email/request/', PasswordResetRequestView.as_view()),
    path('reset-email/<str:uidb64>/<str:token>/', PasswordResetView.as_view()),
    
    #
    path('test/<int:pk>/view',add_view,name='addview')
    
]