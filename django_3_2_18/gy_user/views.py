from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View


class BaseUseClassView(View):
    """
    代码可读性好
    类视图相对于函数视图有更高的复用性
    """
    def get(self, request):
        return HttpResponse('ok')

    def post(self, request):
        return HttpResponse('ok')


def user_cookie(request):
    response = HttpResponse('ok')
    response.set_cookie('name', 'gy', max_age=3600)
    return response


def get_cookie(request):
    name = request.COOKIES.get('name')
    print(name)
    return HttpResponse('ok')


def use_session(request):
    request.session['user_id'] = 100
    # 将session数据缓存到redis   将字段响应到客户端浏览器的cookie中
    user_id = request.session.get('user_id')
    print(user_id)

    # request.session.clear()   # 删除值部分
    # request.session.flush()  # 清楚缓存
    # request.session.set_expiry(value='')   # 设置session的有效期  默认为两周  通过在settings.py中设置SESSION_COOKIE_AGE来设置全局默认值
    # del request.session['建']  # 删除一个键值对
    return HttpResponse('ok')
