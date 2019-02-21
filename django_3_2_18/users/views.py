import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.  视图


# /user/index/
def index(request):
    """
    index视图部分
    :param request: 接收到的请求对象
    :return: 响应对象
    """
    return HttpResponse('hello world!')


def weather(request, city, year):
    print('city=%s' % city)
    print('year=%s' % year)
    return HttpResponse('ok!')


def weather1(request, city, year):
    print('city=%s' % city)
    print('year=%s' % year)
    return HttpResponse('ok!  weather1! ')


def weather2(request, city, year):
    print('city=%s' % city)
    print('year=%s' % year)

    a = request.GET.get('a')
    b = request.GET.get('b')
    a_list = request.GET.getlist('a')
    print(a, b, a_list)
    return HttpResponse('ok!  weather1! ')


def get_post_params(request):
    # POST请求获取表单数据
    a = request.POST.get('a')
    b = request.POST.get('b')
    a_list = request.POST.getlist('a')
    print(a, b, a_list)

    return HttpResponse('get_post')


def get_body_json(request):
    json_str = request.body.decode()
    req_data = json.loads(json_str)

    print(request.META['CONTENT_TYPE'])
    print(request.META['SERVER_NAME'])

    print(request.method)
    print(request.user)
    print(request.encoding)
    print(request.path)
    print(request.files)

    print(req_data['a'])
    print(req_data['b'])

    return HttpResponse('OK get_body')


# 自定义响应体
def response_json(request):
    json_dict = {'name': 'gy', 'age': 12}
    # return HttpResponse('OK', content_type='text/html', status=200)
    return JsonResponse(json_dict)


