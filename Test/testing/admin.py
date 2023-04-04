from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Category)
admin.site.register(Test)
admin.site.register(User)
admin.site.register(UserStatistics)
admin.site.register(Questions)
admin.site.register(UserProfile)
admin.site.register(Likes)
admin.site.register(Comments)
admin.site.register(Answer)
admin.site.register(Score)
admin.site.register(ViewsCount)