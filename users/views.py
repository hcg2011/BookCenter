from django.shortcuts import render, redirect
# Create your views here.
from django.urls import reverse

from users.models import Passport


def register(request):
    return render(request, 'users/register.html')


def register_handle(req):
    username = req.POST.get('user_name')
    password = req.POST.get('pwd')
    email = req.POST.get('email')
    if not all([username, password, email]):
        return render(req, 'users/register.html', {'errmsg': '参数不能为空'})
    Passport.objects.create(username=username, password=password, email=email)
    try:
        Passport.objects.add_one_passport(username=username, password=password, email=email)
    except Exception as e:
        print("e: ", e)
        # return render(req, 'users/register.html', {'errmsg': '用户名已存在！'})
    return redirect(reverse('user:register'))
