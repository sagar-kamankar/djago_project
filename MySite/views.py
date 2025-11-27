from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from .forms import userForms,marksheetForm
from Service.models import Service
from news.models import News 
from contactenquiry.models import contactEnquiry
from django.core.paginator import Paginator


def homePage(request):
    newsData=News.objects.all()

    # serviceData=Service.objects.all().order_by("-service_title")   #[:3]-limit set   #dash(- we use for descending order)
    # if request.method=="GET":
    #     st=request.GET.get('servicename')
    #     if st!=None:
    #         serviceData=Service.objects.filter(service_title__icontains=st)
    serviceData=Service.objects.all()
    paginator=Paginator(serviceData,2)
    page_number=request.GET.get("page")
    ServiceDataFinal=paginator.get_page(page_number)
    totalPages=ServiceDataFinal.paginator.num_pages

    data={
           "serviceData":ServiceDataFinal,
           "newsData":newsData,
           "lastpage":totalPages,
           "total_pages":[n+1 for n in range(totalPages)]
    }

    return render(request,"index.html",data)

def newsDetails(request,slug):
    newsDetail=News.objects.get(news_slug=slug)
    data={"newsDetail":newsDetail}

    return render(request,"newsdetails.html",data)

def aboutUs(request):
    if request.method=="GET":
        output=request.GET.get('output')
    return render(request,"aboutus.html",{'output':output})


def services(request):
    return render(request,"services.html")

def contact(request):
    return render(request,"contact.html")

def saveEnquiry(request):
    if request.method=="POST":
        print(request.method)
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        message=request.POST.get('message')
        en=contactEnquiry(name=name,email=email,phone=phone,message=message)
        print(en)
        en.save()
    return render(request,"contact.html")


def courseName(request,coursename):
    return HttpResponse(f"we having course <b> {coursename} </b>")


def slugUrl(request,name):
    return HttpResponse(f"{name}")


def studentname(request,studentname,coursename):
    return HttpResponse(f"we are student {studentname} having course {coursename}")

def userForm(request):
    fn=userForms()
    dict1={'forms':fn}
    n=0
    
    try:
        if (request.method=="POST"):
            # n1=int(request.GET['num1'])
            # n2=int(request.GET['num2'])
            # n1=int(request.GET.get('num1'))
            # n2=int(request.GET.get('num2'))
            n1=int(request.POST['num1'])
            n2=int(request.POST['num2'])
            n=n1+n2
            dict1={
                'n1':n1,
                'n2':n2,
                'output':n,
                'forms':fn
            }
            url=f"/about-us/?output={n}"
            return HttpResponseRedirect(url)    
        
    except:
        pass    
    return render(request,"userform.html",dict1)
def submitform(request):
    dict1={}
    n=0
    try:
        if (request.method=="POST"):
            # n1=int(request.GET['num1'])
            # n2=int(request.GET['num2'])
            # n1=int(request.GET.get('num1'))
            # n2=int(request.GET.get('num2'))
            n1=int(request.POST['num1'])
            n2=int(request.POST['num2'])
            n=n1+n2
            dict1={
                'n1':n1,
                'n2':n2,
                'output':n
            }
            return HttpResponse(n)    
        
    except:
        pass 

def calculator(request):
    c=""
    d1={}
    try:
        if request.method=="POST":
            n1=eval(request.POST['num1'])
            n2=eval(request.POST['num2'])
            opr=request.POST['opr']
            if opr=="+":
                print(c)
                c=n1+n2
                print(c)
            elif opr=="-":
                c=n1-n2
            elif opr=="*":
                c=n1*n2
            elif opr=="/":
                c=n1/n2


        d1={"n1":n1,
            "n2":n2,
            "Output":c
            }    

    except Exception as e:
        print(f"e:{e}")    

    return render(request,"calculator.html",d1) 

def checknumber(request):
    result=None
    n=""
    try:
        if request.method=="POST":
            if request.POST["num1"]=="":
                return render(request,"evenodd.html",{"error":True})
            n=int(request.POST['num1'])
            if n % 2 == 0:
                result=f"{n} is even"
            
            else:
                result=f"{n} is odd"
            



    except Exception as e:
        print(e)   
    return render(request,"evenodd.html",{"result":result,"n":n})      


def marksheet(request):
    # fn=marksheetForm()
    dict1={}
    try:
        if request.method=="POST":
            subject1=int(request.POST.get("Subject1",0))
            subject2=int(request.POST.get("Subject2",0))
            subject3=int(request.POST.get("Subject3",0))
            subject4=int(request.POST.get("Subject4",0))
            subject5=int(request.POST.get("Subject5",0))

            total=(subject1+subject2+subject3+subject4+subject5)
            percentage=(total/5)

            if percentage>60:
                d="First Division"
            elif percentage>48:
                d="Second Division"
            elif percentage>35:
                d="Third Division"
            else:
                d="Fail"            

        dict1={
                "total":total,
                "percentage":percentage,
                'Subject1':subject1,
                "Subject2":subject2,
                "Subject3":subject3,
                "Subject4":subject4,
                "Subject5":subject5,
                "div":d

        }    

    except Exception as e:
        print(e)    

    return render(request,"marksheet.html",dict1)     

