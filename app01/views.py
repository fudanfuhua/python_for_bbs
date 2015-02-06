from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import models
from django.contrib import auth
from gluon.contrib.pymysql.constants.ER import USERNAME
from django.contrib import comments

# Create your views here.

def index(request):
 # default return title, retun table  first zhiduan.
    bbs_list = models.BBS.objects.all()
#   print [p for p in bbs_list]
    return render_to_response('index.html', {
                                             'bbs_list': bbs_list,
                                             'user': request.user,
                                             })
                                                                                                                        # let request.user  to web page
def bbs_detail(request, bbs_id):
# default return title
#    print bbs_id
    bbs = models.BBS.objects.get(id=bbs_id)
    print bbs.id
# if your don not plus id, default print bbs.title de  first  zhi,
    return render_to_response('bbs_detail.html',{'bbs_obj':bbs,"user":request.user})
                                                                                                                           # let request.user  to web page

def sub_comment(request):
    print request.POST
    bbs_id =  request.POST.get("bbs_id")
    comment = request.POST.get('comment_content')
 
    comments.models.Comment.objects.create(
                                         content_type_id = 7,
                                         object_pk = bbs_id,
                                         site_id = 1,
                                         user = request.user,
                                        comment = comment,
                                         )
    return  HttpResponseRedirect('/detail/%s' % bbs_id )

###################below is user de yonghu renzhengxitong#############################

def account_login(request):
    print request.GET
    username = request.GET.get('username')
    password = request.GET.get('password')
    user = auth.authenticate(username=username, password=password)
    # try this username is ok? if the username is ok, return user = None.
    print user
    if user is  not None:
        if user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect('/')
    else:
        return render_to_response('login.html', {"login_err" : "wrong username or password "})
        
def logout_views(request):
    user = request.user
    print user
    auth.logout(request)
    return HttpResponse("<b>%s</b>  logged out!  <br> <a href='/login'>Re_login</a>" % user)
#return not html page,just data.

def login(request):
    return render_to_response('login.html')
# return html page

########################bbs de mkaing and bbs content de uploadf##########################
def pub(request):
       return render_to_response('pub.html')

def bbs_sub(request):
    print "====>" , request.POST.get('content')
    content = request.POST.get('content')
    author = models.Bbs_User.objects.get(user__username=request.user)
                                                                                #this place get username from database table Bbs_User, most import is double xiahuaxian
    models.BBS.objects.create(
    	title = 'TEST TITLE',
    	summary = 'HAHA',
    	content = content,
    	author = author,
        view_count = 1,
        ranking = 1,
    )
    return HttpResponse('YES')
    

