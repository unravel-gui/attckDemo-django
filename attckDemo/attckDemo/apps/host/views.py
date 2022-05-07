from django.shortcuts import render

# Create your views here.
from django.views import View
from attckDemo.utils.response_code import RETCODE
from django import http
from host.models import Host
import json
import ast

class HostRecDataView(View):
    """判断调用函数"""

    def get(self, request, tablename):
        print("get")
        # self.post(request, tablename)
        print(tablename)
        return http.HttpResponse("index")


    def post(self, request, tablename):
        print("post")
        print(tablename)
        self.Host(request)
        # 响应结果
        return http.JsonResponse({'code': RETCODE.OK, 'errmsg': 'OK'})

    def Host(self, request):
        print("进入Get Host")
        # 接收json列表
        jsonData = json.loads(request.body.decode())
        if jsonData is None:
            return
        # 一条记录写一次
        print(jsonData)
        # 字符串转字典
        jsonData = ast.literal_eval(jsonData)
        Auther = jsonData["Auther"]
        hostip = jsonData["hostip"]
        Email = jsonData["Email"]
        Active = jsonData["Active"]
        record_time = jsonData["record_time"]


        try:
            Host.objects.create(hostip=hostip, Email=Email, Auther=Auther, Active=Active, record_time=record_time)
        except Exception as e:
            print(e)
            return http.HttpResponseServerError('hostinfo数据入库失败')


