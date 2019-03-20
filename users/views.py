from django.http import JsonResponse
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
    # Passport.objects.create(username=username, password=password, email=email)
    try:
        Passport.objects.add_one_passport(username=username, password=password, email=email)
    except Exception as e:
        print("e: ", e)
        return render(req, 'users/register.html', {'errmsg': '用户名已存在！'})
    return redirect(reverse('books:index'))


def login(req):
    username = req.COOKIES.get("username")
    if (username):
        checked = 'checked'
    else:
        checked = ''
        username = ''
    context = {
        'username': username,
        'checked': checked
    }
    return render(req, 'users/login.html', context)


def login_check(req):
    username = req.POST.get('username')
    password = req.POST.get('password')
    remember = req.POST.get('remember')
    if not all([username, password, remember]):
        return JsonResponse({'res': 2})
    passport = Passport.objects.get_one_passport(username=username, password=password)
    if passport:
        next_url = reverse('books:index')
        jres = JsonResponse({'res': 1, 'next_url': next_url})
        if remember:
            jres.set_cookie("username", username, max_age=7 * 24 * 3600)
        else:
            jres.delete_cookie("username")
        req.session['islogin'] = True
        req.session['username'] = username
        req.session['passport_id'] = passport.id
        return jres
    else:
        # 用户名或密码错误
        return JsonResponse({'res': 0})


def logout(req):
    req.session.flush()
    return redirect(reverse("books:index"))
