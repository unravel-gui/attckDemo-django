import sys

from django.shortcuts import render

# Create your views here.
from django.views import View
from django import http
# 迁移数据使用这个
from attckDemo.utils.response_code import RETCODE
from utils.tablesname import tablesdict
# 正常运行使用这个
# from utils.response_code import RETCODE
import logcat.models as md
import ast
import json
from host.models import Host, Kafka
from kafka import KafkaConsumer

class LogcatRecDataView(View):
    """判断调用函数"""

    def get(self, request):
        print("get")
        return http.HttpResponse("index")

    def post(self, request):
        print("post")
        jsonobj = json.loads(request.body)
        try:
            data = jsonobj["data"]
        except Exception:
            try:
                jsonobj = ast.literal_eval(jsonobj)
                data = jsonobj["data"]
                tablename = jsonobj["tablename"]
            except Exception as e:
                print(e)
        # 存储数据

        print("插入表" + tablesdict[tablename])
        res = save(tablesdict[tablename], data)
        if res:
            return http.HttpResponseServerError('数据入库失败')
        # 响应结果
        return http.JsonResponse({'code': RETCODE.OK, 'errmsg': 'ok'})
        # return render(request, "index.html")


def save(topic, data):
    print("进入save")
    """
    利用反射将数据入库
    :param topic: 主题，由表名区分
    :param msg: 数据
    :return:
    """
    cnt = 0
    for param in data:
        try:
            # topic 为记录名
            hostip = Host.objects.filter(hostip=param["hostip"])
            if len(hostip) == 0:
                print("hostip不存在")
                return -1
            # 目前考虑一个用户一条数据
            param["hostip"] = hostip[0]
            # print("第" + str(cnt) + "条数据")
            # print(param)
            AClass = getattr(md, topic)
            getattr(AClass.objects, "create")(**param)
            cnt += 1
        except Exception as e:
            print(e)
            return -1

    print(topic + "成功入库" + str(cnt) + "条记录")
    return 0