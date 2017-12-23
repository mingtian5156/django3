from django.shortcuts import render,redirect
from django.http import JsonResponse
from df_user.user_decorator import login_dec
from .models import *

@login_dec
def cart(request):
	uid = request.session['user_id']
	carts = CartInfo.objects.filter(user_id=uid)
	context = {'title':'gouwuche',
	           'page_name':1,
	           'carts':carts  }
	return render(request,'df_cart/cart.html',context)

@login_dec
def add(request,gid,count):
    #yonghuid goumai gid,shuliang wei count
    uid = request.session['user_id']
    gid = int(gid)
    count = int(count)
    carts = CartInfo.objects.filter(user_id=uid,goods_id=gid)
    if len(carts) >= 1:
    	cart = carts[0]
    	cart.count = cart.count + count
    else:
    	cart = CartInfo()
    	cart.user_id = uid
    	cart.goods_id = gid
    	cart.count = count
    cart.save()
    #if ajax
    if request.is_ajax():
    	count = CartInfo.objects.filter(user_id=request.session[user_name])
    	return JsonResponse({'count':count})
    else:
    	return redirect('/cart/')
    return render(reuqest,'',context)

@login_dec
def edit(request,cart_id,count):
	try:
		cart = CartInfo.objects.get(pk=int(cart_id))
		count1 = cart.count = int(count)
		cart.save()
		data = {'ok',0}
	except Exception as e:    
	    data = {'ok',count1}
	return JsonResponse(data)

@login_dec
def delete(request,cart_id):
    try:
        cart = CartInfo.objects.get(pk=int(cart_id))
        cart.delete()
        data = {'ok':1}
    except Exception as e:    
        data = {'ok',0}
    return JsonResponse(data)














