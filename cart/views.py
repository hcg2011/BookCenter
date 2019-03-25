from django.http import JsonResponse
# Create your views here.
from django_redis import get_redis_connection

from books.models import Books
from utils.decorators import login_required


@login_required
def cart_add(req):
    books_id = req.POST.get("books_id")
    books_count = req.POST.get("books_count")
    if not all([books_count, books_id]):
        return JsonResponse({'res': 1, 'errmsg': '数据不完整'})
    book = Books.objects.get(books_id)
    if book is None:
        return JsonResponse({'res': 2, 'errmsg': '商品不存在'})
    try:
        count = int(books_count)
    except Exception as e:
        return JsonResponse({'res': 3, 'errmsg': '商品数量必须为数字'})
    conn = get_redis_connection()
    cart_key = 'cart_%d' % req.session.get('passport_id')
    res = conn.hget(cart_key, books_id)
    if res is None:  # 如果用户的购车中没有添加过该商品，则添加数据
        res = count
    else:  # 如果用户的购车中已经添加过该商品，则累计商品数目
        res = int(res) + count
    if res > book.stock:
        # 库存不足
        return JsonResponse({'res': 4, 'errmsg': '商品库存不足'})
    else:
        conn.hset(cart_key, books_id, res)
    return JsonResponse({'res': 5})


def cart_count(req):
    conn = get_redis_connection()
    cart_key = 'cart_%d' % req.session.get('passport_id')
    # res = conn.hlen(cart_key) 显示商品的条目数
    res = 0
    res_list = conn.hvals(cart_key)

    for i in res_list:
        res += int(i)
    return JsonResponse({'res': res})
