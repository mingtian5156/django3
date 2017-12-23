from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from .models import *
from hashlib import sha1
from .user_decorator import login_dec
from df_goods.models import *


# Create your views here.
def register(request):
    return render(request,'df_user/register.html')

def register_handle(request):
    #jeishou yonghu  shuru
    post=request.POST
    uname = post.get('user_name')
    upwd = post.get('pwd')
    upwd2 = post.get('cpwd')
    uemail = post.get('email')
    #panduan liangci mima
    if upwd != upwd2:
        return redirect('/user/register/')
    #jiami
    s1 = sha1()
    s1.update(upwd.encode('utf-8'))
    upwd3 = s1.hexdigest()
    #chuangjian duixiang
    user = UserInfo()
    user.uname = uname
    user.upwd = upwd3
    user.uemail = uemail
    user.save()
    #dzhucechenggong zhuandaodelujiemian
    return redirect('/user/login/')

def register_exist(request):
    uname = request.GET.get('uname')
    count = UserInfo.objects.filter(uname=uname).count()
    return JsonResponse({'count':count})

def login(request):
    uname = request.COOKIES.get('uname','')
    context = {'title':'yonghudenglu','error_name':0,'error_pwd':0,'uname':uname}
    return render(request,'df_user/login.html',context)

def login_handle(request):
    post = request.POST
    uname = post.get('uname')
    upwd = post.get('pwd')
    jizhu = post.get('jizhu',0)
    users = UserInfo.objects.filter(uname=uname)
    
    if len(users) == 1:
        s1 = sha1()
        s1.update(upwd.encode('utf-8'))
        if s1.hexdigest() == users[0].upwd:
            url = request.COOKIES.get('url','/')
            red = HttpResponseRedirect(url)
            if jizhu != 0:
                red.set_cookie('uname',uname)
            else:
                red.set_cookie('uname','',max_age=-1)
            request.session['user_id'] = users[0].id
            request.session['user_name'] = uname
            return red
        else:
            context = {'title':'yonghudenglu','error_name':0,'error_pwd':1,'uname':uname,'upwd':upwd}
            return render(request,'df_user/login.html',context)
    else:
        context = {'title':'yonghudenglu','error_name':1,'error_pwd':0,'uname':uname,'upwd':upwd}
        return render(request,'df_user/login.html',context)
def logout(request):
    request.session.flush()
    return redirect('/')

@login_dec
def info(request):
    user_email = UserInfo.objects.get(id=request.session['user_id']).uemail
    goods_ids = request.COOKIES.get('goods_ids','1,2,3,4,5')
    goods_ids1 = goods_ids.split(',')   
    goods_list = []
    for goods_id in goods_ids1:
        goods_list.append(GoodInfo.objects.get(id=int(goods_id)))
    print(goods_list)
    context = {'title':'yonghuzhongxin',
            'user_email':user_email,
            'user_name':request.session['user_name'],
            'page_name':1,
            'goods_list':goods_list,
            }
    return render(request,'df_user/user_center_info.html',context)

@login_dec
def order(request):
    context = {'title':'yonghuzhongxin',
               'user_name':request.session['user_name']}     
    return render(request,'df_user/user_center_order.html',context)

@login_dec
def site(request):
    user = UserInfo.objects.get(id=request.session['user_id'])
    if request.method == 'POST':
        post = request.POST
        user.upostname = post.get('upostname')
        user.uaddress = post.get('upostcode')
        user.uphone = post.get('uphonw')
        user.save()
    context = {'title':'yonghuzhongxin',
                'page_name':1,
                'user':user,
                'user_name':request.session['user_name']}
    return render(request,'df_user/user_center_site.html',context)