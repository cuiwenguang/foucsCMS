# encoding:utf-8
from django.shortcuts import HttpResponse,render
from requests.auth import HTTPBasicAuth
import requests

def test(request):
    url = 'http://127.0.0.1:8000/oauth/token/'

    token_request_data = {
        'grant_type': 'password',
        'username': 'admin',
        'password': 'by123456',
    }
    client_id = 'VpL2mTHlynQdHbHNFbjH2ajFuvSBGZ7pTXbfLaB0'
    client_secret = '3zxGWfe0OFkFIA8wm3cx12ix9Btcv4jVdZabCCsZmEQaB3N8hGg2JiD5Vw6jue3HZl5mpZ46hLm7aFtBV5J1wxyl5TJGM4nir76Lr8YH6Los2KoaNyImO2v40ixcWJGW'

    auth_header = HTTPBasicAuth(client_id, client_secret)
    res = requests.post(url,  data=token_request_data, auth=auth_header)

    return HttpResponse(res.text)


def login(request):
    '''登录'''
    pass

def register(request):
    '''注册'''
    pass

def update_Info(request):
    '''修改个人信息'''
    pass

def update_password(request):
    '''修改密码'''
    pass

def bind_paypal(request):
    '''绑定网银'''
    pass

def update_pay_password(request):
    '''修改提现密码'''
    pass

def my_Favorites(request):
    '''我的收藏'''
    pass

def my_comments(request):
    '''我的评论'''
    pass

def my_subscribe_channels(request):
    '''我订阅的频道'''
    pass