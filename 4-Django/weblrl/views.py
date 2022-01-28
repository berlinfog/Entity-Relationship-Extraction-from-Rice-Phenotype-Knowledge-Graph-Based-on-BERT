from django.shortcuts import render,redirect
from weblrl import models
from .forms import UserForm
from .forms import RegisterForm

def index(request):
    pass
    return render(request,'index.html')

def login(request):
    # all1=[]
    if request.session.get('is_login',None):
        return redirect('/')

    if request.method == "POST":
        login_form = UserForm(request.POST)
        message = "请检查填写的内容！"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = models.Usermsg.objects.get(name=username)
                # all1=str(models.Usermsg.objects.all())
                if user.passwd == password:
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.name
                    return redirect('/detail')
                else:
                    message = "密码不正确！"
            except:
                message ="用户不存在！"
        return render(request, 'login.html', locals())

    login_form = UserForm()
    return render(request, 'login.html', locals())

def register(request):
    if request.session.get('is_login', None):
        return redirect("/")
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():  # 获取数据
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            email = register_form.cleaned_data['email']
            sex = register_form.cleaned_data['sex']
            if password1 != password2:  # 判断两次密码是否相同
                message = "两次输入的密码不同！"
                return render(request, 'login/register.html', locals())
            else:
                same_name_user = models.Usermsg.objects.filter(name=username)
                if same_name_user:  # 用户名唯一
                    message = '用户已经存在，请重新选择用户名！'
                    return render(request, 'login/register.html', locals())
                same_email_user = models.Usermsg.objects.filter(email=email)
                if same_email_user:  # 邮箱地址唯一
                    message = '该邮箱地址已被注册，请使用别的邮箱！'
                    return render(request, 'login/register.html', locals())

                # 当一切都OK的情况下，创建新用户

                new_user = models.Usermsg.objects.create()
                new_user.name = username
                new_user.passwd = password1
                new_user.email = email
                new_user.sex = sex
                new_user.save()
                return redirect('/login')  # 自动跳转到登录页面
    register_form = RegisterForm()
    return render(request, 'register.html', locals())

def logout(request):
    if not request.session.get('is_login', None):
        # 如果本来就未登录，也就没有登出一说
        return redirect("/")
    request.session.flush()
    return redirect("/")

def detail(request):
    relation = models.relation.objects.values('sentence','entity1','entity2','result').filter(name=request.session['user_name'])
    relation1=list(relation)
    entity = models.entity.objects.values('entity','friend').filter(name=request.session['user_name'])
    entity1=list(entity)
    question = models.question.objects.values('question','answer').filter(name=request.session['user_name'])
    question1=list(question)

    return render(request,'detail.html',{"relation":relation1,"entity":entity1,"question":question1})