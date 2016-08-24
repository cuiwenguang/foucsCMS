# encoding:utf-8
from django.contrib.auth.models import User
from django.conf.urls import url
from tastypie.resources import ModelResource
from tastypie.serializers import Serializer
from tastypie.utils import trailing_slash
from oauth2_provider.views.base import TokenView

class AuthResource(ModelResource):
    '''
        用户认证：注册，登录，注销
    '''
    class Meta:
        queryset = User.objects.all()
        allowed_methods = ['post', 'put']
        resource_name = 'auth'
        serializer = Serializer(formats=['json'])


    def prepend_urls(self):
        return [
            url(r"^(?P<resource_name>%s)/login%s$" %
                (self._meta.resource_name, trailing_slash()),
                self.wrap_view('login'), name="api_login"),  # 用户登录
            url(r'^(?P<resource_name>%s)/register%s$' %
                (self._meta.resource_name, trailing_slash()),
                self.wrap_view('register'), name='api_register'),  # 用户注册
        ]

    def login(self, request, *args, **kwargs):
        pass

    def register(self, request, **kwargs):
        pass
