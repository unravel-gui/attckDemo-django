from host.models import Host
# from logcat.models import System_info
import logcat.models as md
import json
import ast


class logcatReflection(object):

    def system_info(self, request):
        print("进入Get system_info")
        # 接收json列表
        jsonobj = json.loads(request.body.decode())
        record_time = jsonobj["record_time"]
        hostip = jsonobj["hostip"]
        jsonDatas = jsonobj['system_info']
        if jsonDatas is None:
            return
        # print(jsonDatas)
        for jsonData in jsonDatas:
            # 一条记录写一次
            # print(jsonData)
            # 字符串转字典
            jsonData = ast.literal_eval(jsonData)
            cpu_brand = jsonData['cpu_brand']
            cpu_type = jsonData['cpu_type']
            physical_memory = jsonData['physical_memory']
            print(hostip)
            try:
                hostip = Host.objects.filter(HostIP=hostip)[0]
                md.SystemInfo.objects.create(hostip=hostip,
                                             cpu_brand=cpu_brand, cpu_type=cpu_type, physical_memory=physical_memory,
                                             record_time=record_time)
            except IndexError as e:
                # 外键不存在
                print(e)
                print("外键不存在")
                return -1
            except Exception as e:
                print(e)
                return -1

            """
    
            try:
                # 每次都写入
                systeminfoData = System_info()
                # 外键特殊一点, 需要该值存在
                systeminfoData.hostip = Host.objects.filter(HostIP=hostip)[0]
                systeminfoData.name = computer_name
                systeminfoData.cpu_type = cpu_type
                systeminfoData.cpu_brand = cpu_brand
                systeminfoData.record_time = record_time
                systeminfoData.physical_memory = physical_memory
                systeminfoData.save()
            except Exception as e:
                print(e)
                return http.HttpResponseServerError('systeminfo数据入库失败')
            """
        # 响应结果
        return 0
