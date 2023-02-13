from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import render,redirect
from coffee.forms import EmpForm
from django.shortcuts import render,redirect
from coffee.models import Student
from coffee import  models
from .models import Image
from .forms import ImageForm









def index(request):
    return render(request,'index.html')
def review(request):
    return render(request,'review.html')



def cl(request):
    if request.method == "POST":
        form = EmpForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/show")
            except:
                pass
    else:
        form = EmpForm()
    return render(request,'cl.html',{'gaurav':form})

def show(request):
    employees = Student.objects.all()
    return render(request,"show.html",{'gaurav':employees})

def destroy(request,id):
    employee = Student.objects.get(id=id)
    employee.delete()
    return redirect("/show")

def edit(request,id):
    employee = Student.objects.get(id=id)
    return render(request,'edit.html',{'employee':employee})

def update(request,id):
    employee = Student.objects.get(id=id)

    form = EmpForm(request.POST,instance=employee)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request,'edit.html',{'employee':employee})


def login(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')
        obj_user = models.WangUser.objects.filter(username=username,password=password)
        if obj_user:
            return redirect('il')
        error = 'wrong username and password'
    return render(request,'login.html',locals())
def il(request):
    return render(request,'il.html')
def rl(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_list = models.WangUser.objects.filter(username=username) # filter-comparison #agr username already exist krega
        #yha hm html ka form bnenge sre fiels get krli

        error_name = []
        if user_list:
            error_name='the user already exist'
            return render(request,'rl.html',{'error_name':error_name}) #error ko render
        else:
            username = models.WangUser.objects.create(username=username,password=password,email=email)
            username.save() #wang model h data phoch gye

        return redirect('login') #registration hone ke bd login phoch jye

    return render(request,'rl.html')  #koi kmi ha to vhi rhe

def ImageUploaderProject(request):
    if request.method =='POST':
        fm = ImageForm(request.POST,request.FILES)
        if fm.is_valid():
            fm.save()
            messages.info(request,'image successfully upload')
            return HttpResponseRedirect('/')
    fm = ImageForm()
    img = Image.objects.all()

    return render(request,'enroll/image.html',{'img':img,'fm':fm})
    #fm or img name ki key me data uth uth ke arha ha



