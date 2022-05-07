import json
import time

import osquery
import requests
import socket
from tablesname import tablesname


"""
    查询成功的响应
    (status=ExtensionStatus(code=0, message='OK', uuid=0)
    缺少 条件字段 的响应
    ExtensionResponse(status=ExtensionStatus(code=1, message='constraint failed', uuid=0), response=[])
    windows 下的 shellbags
    'utf-8' codec can't decode byte 0x81 in position 19: invalid start byte
    
    本地windows执行完后
    print(self.list)
            print(self.sleeplist)
            print(self.needcolumn)
    一共有 106 张表，成功获得 66 张表的数据
    本地的空表   ['atom_packages', 'azure_instance_metadata', 'azure_instance_tags', 'background_activities_moderator', 'bitlocker_info', 'carves', 'ec2_instance_metadata', 'ec2_instance_tags', 'intel_me_info', 'ntfs_journal_events', 'osquery_packs', 'osquery_schedule', 'powershell_events', 'prefetch', 'ssh_configs', 'tpm_info', 'user_ssh_keys', 'windows_crashes', 'windows_events', 'wmi_bios_info', 'wmi_cli_event_consumers', 'wmi_script_event_consumers', 'ycloud_instance_metadata']
    执行会卡住   ['autoexec', 'ie_extensions', 'pipes']
    需要条件字段才能执行查询  ['authenticode', 'curl', 'curl_certificate', 'device_file', 'device_hash', 'device_partitions', 'file', 'hash', 'ntfs_acl_permissions', 'shortcut_files', 'windows_eventlog', 'yara']
    执行报错     ['shellbags', 'shimcache']
"""

class Agent(object):

    def __init__(self):
        self.url = "http://127.0.0.1:8000/"
        self.proxies = {'http': 'http://127.0.0.1:8080', 'https': 'https://127.0.0.1:8080'}
        self.hostip = self.get_host_ip()
        self.tables = tablesname
        # 以下表查询时会卡死
        self.sleeplist = ["autoexec", "ie_extensions", "pipes"]
        # 查询需要 条件字段信息
        self.needcolumn = []
        self.list = []
        self.errlist = []


    @staticmethod
    def get_host_ip():
        s = ''
        try:
            # 通过谷歌dns服务器查询IP
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(('8.8.8.8', 53))
            ip = s.getsockname()[0]
        finally:
            s.close()
        return ip


    @staticmethod
    def Getinput():
        authname = input("请输入管理员名称")
        email = input("请输入邮箱")
        return authname, email


    def attachData(self, data, tablename):
        if data is None:
            return None
        param_list = []
        # data 为一个列表
        for l in data:
            # 一条记录
            l["hostip"] = self.hostip
            l["record_time"] = str(int(time.time()))
            # print(l)
            param_list.append(l)
        meta = json.dumps({"data": param_list, "tablename": tablename})
        return meta




    def Post(self, meta, url):
        if meta is None:
            return
        res = requests.post(url=url, json=meta)
        print(res.status_code)


    def Host(self):
        """
        主机信息
        :return:
        """
        authname, email = self.Getinput()
        paramdict = {"hostip": self.hostip, "Auther": authname, "Email": email, "Active": "1", "record_time": str(int(time.time()))}
        data = json.dumps(paramdict)
        url = self.url + "host/host"
        self.Post( data, url)


    def getData(self, tablename):
        """
        获得表名，拼接成sql，带入查询，返回数据， 后期可根据不同类型表进行修改
        :param tablename:
        :return:
        """
        sql = "select * from %s;" % tablename
        print(sql)
        instance = osquery.SpawnInstance()
        instance.open()
        try:
            ret = instance.client.query(sql)
        except Exception as e:
            self.errlist.append(tablename)
            return None
        length = len(ret.response)
        # print("状态码为: " + str(ret.status.code))
        if ret.status.code:
            self.needcolumn.append(tablename)
            return None
        if length == 0:
            self.list.append(tablename)

        if not ret.response:
            return None
        return ret.response


    def run(self):
        # self.Host()
        if True:
        # while True:
            cnt = 0
            for table in tablesname:
                if table in self.sleeplist:
                    continue
                # 获得原始数据
                data = self.getData(table)
                # 加工数据
                meta = self.attachData(data, table)
                url = self.url + "logcat/%s" % table
                if meta is None:
                    continue
                cnt += 1
                print(cnt)
                self.Post(meta, url)
            string = "一共有 "+ str(len(self.tables)) + " 张表，成功获得 " + str(cnt) + " 张表的数据"
            # print(string)
            # print(self.list)
            # print(self.sleeplist)
            # print(self.needcolumn)
            # print(self.errlist)
        # time.sleep(3600*30)


# 测试
def test():
    sql = "select * from shellbags;"
    print(sql)
    instance = osquery.SpawnInstance()
    instance.open()
    try:
        ret = instance.client.query(sql)
    except Exception as e:
        exit("ok")

    print(ret)
    print(ret.status.code)
    print(ret.response)


def main():
    try:
        dd = Agent()
        dd.run()
    except BaseException as e:
        print(e.args[0])


if __name__ == '__main__':
    # test()
    main()
