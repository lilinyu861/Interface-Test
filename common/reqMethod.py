import requests
import json


class RequestMethod:
    """初始化数据"""
    def __init__(self):
        self.data = {}
        self.files = {}

    def get(self, interface_url, params=None):
        """
        get请求
        :param interface_url: 接口地址
        :param params: 接口参数
        :return:
        """
        test_url = interface_url
        try:
            return requests.get(url=test_url, params=params, timeout=60)
        except TimeoutError:
            return print('%s get request timeout!' % test_url)

    def get_with_login_session(self, login_url, interface_url, headers, login_data, params=None, flag='searchCondition'):
        """
        带session的get请求
        :param login_url:  登录地址
        :param interface_url:  接口地址
        :param headers:  报文头
        :param login_data:    登录数据
        :param params:  接口请求参数
        :param flag:
        :return:
        """
        login_url = login_url
        test_url = interface_url
        get_headers = {
            'Content-type': 'multipart/form-data'
        }
        page_headers = {
            'activePage': '1',
            'rowsOnPage': '10'
        }
        try:
            session = requests.Session()
            session.post(url=login_url, headers=headers, data=json.dumps(login_data), timeout=60)
            if flag == 'searchCondition':
                return session.get(url=test_url, headers=get_headers, params=params, timeout=60)
            if flag == 'page':
                return session.get(url=test_url, headers=page_headers, params=params, timeout=60)
            return session.get(url=test_url, params=params, timeout=60)
        except TimeoutError:
            return print('%s get with session request timeout' % test_url)

    def post(self, interface_url, headers=None, data=None):
        """
        post请求
        :param interface_url: 接口地址
        :param headers: 报文头
        :param data: 接口请求参数
        :return: 
        """""
        test_url = interface_url
        try:
            return requests.post(url=test_url, headers=headers, data=json.dumps(data), timeout=60)
        except TimeoutError:
            return print('%s post request timeout!' % test_url)

    def post_with_file(self, interface_url, data, file_path):
        """
        post方法上传文件
        :param interface_url: 接口地址
        :param data: 接口请求参数
        :param file_path: 上传文件地址
        :return:
        """
        test_url = interface_url
        file = {
            'file': open(file_path, 'rb')
        }
        try:
            return requests.post(url=test_url, data=data, files=file, timeout=60)
        except TimeoutError:
            return print('%s post request timeout!' % test_url)

    def post_with_login_session(self, login_url, interface_url, headers, login_data, data, flag='json'):
        """
        带session的post请求
        :param login_url: 登录地址
        :param interface_url: 接口地址
        :param headers: 报文头
        :param login_data: 登录接口请求参数
        :param data: 测试接口请求参数data
        :param flag: flag代表参数类型，默认为'json'
        :return:
        """
        login_url = login_url
        test_url = interface_url
        try:
            session = requests.Session()
            session.post(url=login_url, headers=headers, data=json.dumps(login_data), timeout=60)
            if flag == 'json':
                return session.post(url=test_url, headers=headers, data=json.dumps(data), timeout=60)
            else:
                return session.post(url=test_url, data=json.dumps(data), timeout=60)
        except TimeoutError:
            return print('%s post with session request timeout!' % test_url)

    def delete(self, interface_url, headers=None, data=None):
        """
        定义delete方法请求
        :param interface_url: 接口地址
        :param headers: 报文头
        :param data: 接口请求参数
        :return:
        """
        test_url = interface_url
        try:
            return requests.delete(url=test_url, headers=headers, data=json.dumps(data), timeout=60)
        except TimeoutError:
            return print('%s delete request timeout!' % test_url)

    def delete_with_login_session(self, login_url, interface_url, headers, login_data, data=None, flag='json'):
        """
        带session的delete请求方法
        :param interface_url: 接口地址
        :param headers: 报文头
        :param login_data: 登录参数
        :param data: 接口请求参数
        :param flag:
        :return:
        """
        login_url = login_url
        test_url = interface_url
        try:
            session = requests.Session()
            session.delete(url=login_url, headers=headers, data=json.dumps(login_data), timeout=60)
            if flag == 'json':
                return session.delete(url=test_url, headers=headers, data=json.dumps(data), timeout=60)
            else:
                return session.delete(url=test_url, data=json.dumps(data), timeout=60)
        except TimeoutError:
            return print('%s delete with session request timeout!' % test_url)

    def put(self, interface_url, headers=None, data=None):
        """
        put请求方法
        :param interface_url: 接口地址
        :param headers: 报文头
        :param data: 接口请求参数
        :return:
        """
        test_url = interface_url
        try:
            return requests.put(url=test_url, headers=headers, data=json.dumps(data), timeout=60)
        except TimeoutError:
            return print('%s put request timeout!' % test_url)

    def put_with_login_session(self, login_url, interface_url, headers, login_data, data=None, flag='json'):
        """
        带session的put方法
        :param login_url: 登录接口地址
        :param interface_url: 测试接口地址
        :param headers: 报文头
        :param login_data: 登录数据
        :param data: 接口请求参数
        :param flag:
        :return:
        """
        login_url = login_url
        test_url = interface_url
        try:
            session = requests.Session()
            session.post(url=login_url, headers=headers, data=json.dumps(login_data), timeout=60)
            if flag == 'json':
                return session.put(url=test_url, headers=headers, data=json.dumps(data), timeout=60)
            else:
                return session.put(url=test_url, data=json.dumps(data), timeout=60)
        except TimeoutError:
            return print('%s put with session request timeout!' % test_url)

    def patch(self, interface_url, params=None):
        """
        patch方法请求
        :param interface_url: 接口地址
        :param params: 接口请求参数
        :return:
        """
        test_url = interface_url
        try:
            return requests.patch(url=test_url, params=params, timeout=60)
        except TimeoutError:
            return print('%s patch request timeout!' % test_url)

    def patch_with_login_session(self, login_url, interface_url, headers=None, login_data=None, data=None, flag='json'):
        """
        带session的patch请求方法
        :param login_url: 登录地址
        :param interface_url: 测试接口地址
        :param headers: 报文头
        :param login_data: 登录参数
        :param data: 接口请求参数
        :param flag:
        :return:
        """
        login_url = login_url
        test_url = interface_url
        try:
            session = requests.Session()
            session.post(url=login_url, headers=headers, data=json.dumps(login_data), timeout=60)
            if flag == 'json':
                return session.patch(url=test_url, headers=headers, data=json.dumps(data), timeout=60)
            else:
                return session.patch(url=test_url, data=json.dumps(data), timeout=60)
        except TimeoutError:
            return print('%s patch with session request timeout!' % test_url)

    def head(self, interface_url):
        """
        head请求方法
        :param interface_url: 测试接口地址
        :return:
        """
        test_url = interface_url
        try:
            return requests.head(url=test_url, timeout=60)
        except TimeoutError:
            return print('%s head request timeout!' % test_url)

    def head_with_login_session(self, login_url, interface_url, headers, login_data):
        """
        带session的head请求方法
        :param login_url: 登录接口地址
        :param interface_url: 测试接口地址
        :param headers: 报文头
        :param login_data: 登录参数
        :return:
        """
        login_url = login_url
        test_url = interface_url
        try:
            session = requests.Session()
            session.post(url=login_url, headers=headers, data=json.dumps(login_data), timeout=60)
            return session.head(url=test_url, timeout=60)
        except TimeoutError:
            return print('%s head with login session timeout!' % test_url)

    def options(self, interface_url):
        """
        options请求方法
        :param interface_url: 测试接口地址
        :return:
        """
        test_url = interface_url
        try:
            return requests.options(url=test_url, timeout=60)
        except TimeoutError:
            return print('%s options request timeout!' % test_url)

    def options_with_login_session(self, login_url, interface_url, headers, login_data, data=None):
        """
        带session的options请求方法
        :param login_url: 登录接口地址
        :param interface_url: 测试接口地址
        :param headers: 报文头
        :param login_data: 登录请求参数
        :param data: 接口请求参数
        :return:
        """
        login_url = login_url
        test_url = interface_url
        try:
            session = requests.Session()
            session.post(url=login_url, headers=headers, data=json.dumps(login_data), timeout=60)
            return session.options(url=test_url, timeout=60)
        except TimeoutError:
            return print('%s options with login session timeout!' % test_url)




