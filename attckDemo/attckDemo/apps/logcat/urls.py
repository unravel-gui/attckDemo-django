# logcat 子路由

from django.urls import path, re_path
from . import views

urlpatterns = [
    #
    # re_path(r'^register/$', views.RegisterView.as_view(), name='register'),
    # 通过路由给参数
    re_path(r'^', views.LogcatRecDataView.as_view()),
]



