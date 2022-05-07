# host 子路由

from django.urls import path, re_path
from . import views

urlpatterns = [
    # 通过路由给参数
    re_path(r'^(?P<tablename>[a-zA-Z0-9_-]{2,20})$', views.HostRecDataView.as_view()),
]



