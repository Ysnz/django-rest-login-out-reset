from django.urls import path,include
from django.conf import settings
from . import views
from django.conf.urls.static import static
from viewsets import userviewsets
from rest_framework import routers

router = routers.DefaultRouter()
router.register('user',userviewsets,base_name='user_api')



urlpatterns = [
         path('',views.index,name='index'),
]