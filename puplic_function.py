"""
    author : xiu
    time : 2020.6.2
"""
import re
import logging
import json
import requests
from requests.exceptions import RequestException
from time_update import Configuration

# from hostapp.models import node_management

"""
    这是存储apiURL的调用d
"""


class MyError(Exception):  # 自定义的报错信息展示 MyError
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


class StorageApi:
    def __init__(self, ip, url, item="storage_port", time=None, params=None, headers=None, port=None):
        """
        :param ip: 用户访问ip
        :param url: 用户访问url
        :param item: 用户想访问的配置文件【xxx】 内容 /etc/configuration.ini 默认配置文件目录
        :param time: 请求返回超时时间
        :param params: 请求参数
        :param headers: 请求头
        :param port: 接口的参数值port默认为8086
        """
        self.ip = self._check_ip(ip)
        if not port:
            self.port = Configuration(inifile_bacitmes=item).send_item_back_value()[0][1]
        else:
            self.port = port
        self.url = url  # >>> /api/xxx/xxx/
        self.params = params  # >>> ex:  {name=pxq,age=25,sex=man}
        self.headers = headers
        self.http_url = "http://"
        self.time = time

    def __repr__(self):
        if self.port is None or not self.http_url:
            return '<%s>' % self.__class__.__name__
        return '<%s: %s %r>' % (self.__class__.__name__, self.headers, self.http_url)

    def __str__(self):
        explain = "这是存储{}api接口的调用整合的类".format(self.http_url)
        return explain

    @property
    def url_params_init(self):  # 查看属性
        return self.url, self.params

    @url_params_init.setter  # 添加或设置属性（属性名.setter）
    def url_params_init(self, url, params=None):
        self.url = url
        self.params = params

    def set_url_params(self, url, ip=None, params=None, time=None, port=None):
        if ip:
            self.ip = ip
        self.url = url
        self.params = params
        if time:
            self.time = time
        else:
            self.time = None
        if port:
            self.port = port

    def _check_ip(self, ipAddr):
        compile_ip = re.compile(
            '^(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|[1-9])\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)$')
        if compile_ip.match(ipAddr):
            return ipAddr
        else:
            raise MyError('IP The format is wrong,please enter again,ex <<< 192:xxx:xxx:xxx')

    def _joint_url(self):
        get_url = self.http_url + str(self.ip) + ":" + str(self.port) + self.url
        #  >>>  get_url = http://192.168.4.33:80/api/test
        return get_url

    def get_public_api(self, ):
        try:
            url = self._joint_url()
            if self.params:
                print(url,333333333333333333)
                print(self.params)
                html = requests.get(url, params=self.params, timeout=self.time)
                print(html,3333333333333333333333)
            else:
                html = requests.get(url)
            if html.status_code == 200:
                if html.text:
                    return json.loads(html.text)
                else:
                    return html
        except RequestException:
            print('无法访问%s接口' % self.ip)
            return None

    def print_get_url(self):
        # 打印一下拼接好的请求url地址的路径信息
        get_url = self.http_url + str(self.ip) + ":" + str(self.port) + self.url
        if self.params:
            params = ""
            index = 0
            for k, v in self.params.items():
                if index >= len(self.params) - 1:
                    get_params = str(k) + "=" + str(v)
                else:
                    get_params = str(k) + "=" + str(v) + "&"
                params += get_params
                index += 1
            url = get_url + "?" + params
            return url
        else:
            return get_url


""""""


class GetIP:
    """获取ip"""

    def __str__(self):
        explain = "获取配置文件机器IP"
        return explain

    def __init__(self):
        pass

    @staticmethod
    def get_conf_self_ip():
        # 获取配置文件本机IP
        try:
            oneself_node_ip = Configuration(inifile_bacitmes='a_ip').send_item_back_value()
            self_ip = oneself_node_ip[0][1]
            return self_ip  # >>>  192.168.4.xxx
        except RequestException:
            print('查询配置文件信息失败，请检查配置文件信息ip格式是否有误')
            logging.info('查询配置文件信息失败，请检查配置文件信息ip格式是否有误')

    @staticmethod
    def get_conf_self_node():
        # 获取配置文件本机节点名称
        try:
            oneself_node_ip = Configuration(inifile_bacitmes='a_ip').send_item_back_value()
            self_ip = oneself_node_ip[0][1]
            system_ip_node = Configuration(inifile_bacitmes='node_ip').send_item_back_value()
            for ip_node in system_ip_node:
                if ip_node[1] == self_ip:
                    return ip_node[0]  # >>>  node00
            return None
        except RequestException:
            print('查询配置文件信息失败，请检查配置文件信息节点格式是否有误')
            logging.info('查询配置文件信息失败，请检查配置文件信息节点格式是否有误')

    @staticmethod
    def get_conf_all_ip():
        # 获取机器配置文件所有的IP
        try:
            system_all_ip = Configuration().Detection_of_effective_ip()
            return system_all_ip  # >>>  ['192.168.4.116']
        except RequestException:
            print('查询配置文件信息失败，请检查配置文件信息ip格式是否有误')
            logging.info('查询配置文件信息失败，请检查配置文件信息ip格式是否有误')

    @staticmethod
    def get_conf_all_node():
        # 获取机器配置文件所有的节点名称
        try:
            system_node = Configuration(inifile_bacitmes='node_ip').send_item_back_value()
            node_list = []
            for node_ip in system_node:
                node_list.append(node_ip[0])
            return node_list  # >>>  ['node00']
        except RequestException:
            print('查询配置文件信息失败，请检查配置文件信息节点格式是否有误')
            logging.info('查询配置文件信息失败，请检查配置文件信息节点格式是否有误')

    @staticmethod
    def get_conf_all_node_ip():
        # 获取机器所有的节点和IP
        system_ip = Configuration(inifile_bacitmes='node_ip').send_item_back_value()
        return system_ip  # >>>   [('node00', '192.168.4.116')]

    @staticmethod
    def get_conf_nodename_back_ip(node_name):
        # 发送节点名称，返回ip
        node_ip = Configuration().send_item_back_value()
        for i in node_ip:
            if i[0] == node_name:
                return i[1]  # >>>  192.168.4.xx
        return None

    @staticmethod
    def get_conf_ip_back_nodename(ip):
        # 发送ip，返回节点名称
        node_ip = Configuration().send_item_back_value()
        for i in node_ip:
            if i[1] == ip:
                return i[0]  # >>>  node00
        return None

    # @staticmethod
    # def get_db_all_ip():
    #     try:
    #         node_in_list = []
    #         result = node_management.objects.all().values()
    #         for val in result:
    #             webmaster = eval(val['webmaster'])
    #             node_in_list.append(webmaster['ip'])
    #         return node_in_list
    #     except RequestException:
    #         print('无法获取数据库ip信息')
    #         logging.info('获取节点列表失败')


if __name__ == '__main__':
    pass
    # print(StorageApi(ip='192.168.4.33', url="ffff").get_public_api())
    stor = StorageApi(ip='192.168.4.33', url="/api/test", params={"name": "pxq", "age": 12})
    print(stor._joint_url())
    print(stor.print_get_url())
    # stor.url = "/111111/111111/222222/333333"
    # stor.params = {"ss": 11}
    # stor.api_init = "/111111/111111/222222/333333", {"ss": 11}
    stor.set_url_params(url="/111111/111111/222222/333333", params={"ss": 11})
    # stor.api_init ="/111111/111111/222222/333333",{"ss": 11}
    # stor.api_init(url="/111111/111111/222222/333333", params={"ss": 11})
    print(stor._joint_url())
    # print(GetIP.get_conf_all_ip())
    # print(GetIP.get_self_ip())
    # print(GetIP().get_nodename_back_ip(node_name="txdpxl"))
    # print(GetIP().get_ip_back_nodename(ip="192.168.4.116"))
    # print(Configuration(inifile_bacitmes='storage_port').send_item_back_value()[0][1])
