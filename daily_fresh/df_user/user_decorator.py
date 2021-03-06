from django.http import HttpResponseRedirect
from django.shortcuts import redirect

def login_dec(func):
    def login_fun(request,*args,**kwargs):
        if request.session.has_key('user_id'):
            return func(request,*args,**kwargs)
        else:
            red = HttpResponseRedirect('/user/login/')
            red.set_cookies('url',request.get_full_path())
            return red
    return login_fun
