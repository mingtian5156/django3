from django.shortcuts import render,redirect
from df_user.user_decorator import login_dec
from df_user.models import UserInfo
from df_cart.models import *
from django.db import transaction
from .models import *
from datetime import datetime
from decimal import Decimal


@login_dec
def order(request):
	user = UserInfo.objects.get(id=request.session['user_id'])
    get = request.GET 
    cart_ids = get.getlist('cart_id')
    cart_ids1 = [int(item) for item in cart_ids]
    carts = CartInfo.objects.filter(id__in=cart_ids1)

    context = {'title':'commit',
               'page_name':1,
               'carts':carts,
               'user',:user,
               'cart_ids':','join(cart_ids)}
    return render(request,'df_order/order.html',context)