from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse,JsonResponse
# from .models import Question
import requests

p=''
# Create your views here.
#def index(request):
#   data=Question.objects.order_by('-pub_date')[:5]
#   context={
#       'question_list':data
#   }
#    return render(request, 'index.html', context)

#def detail(request,question_id):
#   return HttpResponse("You are lokking at question %s" % question_id)


def login(request):
    return render(request,'login1.html')

def invalid_login(request):
    return render(request,'invalid_login.html')

def home(request):
    if (request.method)=="POST":
        id1=request.POST['id']
        name=request.POST['username']
        password=request.POST['password']
        det = { 'id':id1,'name':name,'password':password}
        token = requests.post("https://sport-resources-booking-api.herokuapp.com/AdminLogin",det)
        global p
        p = token.json()['access_token']
        if(p=="Invalid Credentials"):
            return redirect('invalid_login')
            #return HttpResponse(p)
        else:
            data = requests.get("https://sport-resources-booking-api.herokuapp.com/ResourcesPresent", headers = {'Authorization':f'Bearer {p}'}) 
            res = data.json()
            context={'data': res,}
            return redirect('api')

def api_call(request):
    global p
    token = requests.post("https://sport-resources-booking-api.herokuapp.com/AdminLogin",data={'id': '12345','name':'Ram','password':'abc12345'} )
    p = token.json()['access_token']
    data = requests.get("https://sport-resources-booking-api.herokuapp.com/ResourcesPresent", headers = {'Authorization':f'Bearer {p}'}) 
    res = data.json()
    if(p==''):
        return redirect('login')
    else:
        context={'data': res,} 
        return render(request,'api.html',context)
def about(request):
    return render(request,'about.html')

def incOne(request):
    id = request.GET['id']

    global p
    td=requests.get('https://sport-resources-booking-api.herokuapp.com/incrementByValue',headers={'Authorization':f'Bearer {p}'},
    data={'id':id,'c':1})
    res = td.json()
    return JsonResponse(res,safe=False)

def decOne(request):
    id = request.GET['id']

    global p
    td=requests.get('https://sport-resources-booking-api.herokuapp.com//decrementByValue',headers={'Authorization':f'Bearer {p}'},
    data={'id':id,'c':1})
    res = td.json()
    return JsonResponse(res,safe=False)

def bookingRequests(request):
    token = requests.post("https://sport-resources-booking-api.herokuapp.com/login",data={'id': '160118733012','password':'abc123'} )
    global p
    p = token.json()['access_token']
    data = requests.get("https://sport-resources-booking-api.herokuapp.com/bookingRequests", headers = {'Authorization':f'Bearer {p}'}) 
    res = data.json()
    context={'data': res,} 
    return render(request,'bookingreq.html',context)

def reject(request):
    id = request.GET['id']

    global p
    td=requests.get('https://sport-resources-booking-api.herokuapp.com/rejectBooking',headers={'Authorization':f'Bearer {p}'},
    data={'id':id})
    res = td.json()
    return JsonResponse(res,safe=False)

def accept(request):
    id = request.GET['id']
    global p
    td=requests.get('https://sport-resources-booking-api.herokuapp.com/issueResource',headers={'Authorization':f'Bearer {p}'},
    data={'id':id})
    res = td.json()
    return JsonResponse(res,safe=False)

def blockedUsers(request):
    global p
    td=requests.get('https://sport-resources-booking-api.herokuapp.com/blockedUsers',headers={'Authorization':f'Bearer {p}'},)
    res = td.json()
    context={'data': res,} 
    return render(request,'blocked.html',context)
    #return JsonResponse(res,safe=False)

def unblock(request):
    id = request.GET['id']
    global p
    td=requests.get('https://sport-resources-booking-api.herokuapp.com/unblockUser',headers={'Authorization':f'Bearer {p}'},
    data={'id':id})
    res = td.json()
    return JsonResponse(res,safe=False)

def His(request):
    global p
    data1 = requests.get("https://sport-resources-booking-api.herokuapp.com/notreturnedHistory", headers = {'Authorization':f'Bearer {p}'})
    data2 = requests.get("https://sport-resources-booking-api.herokuapp.com/returnedHistory", headers = {'Authorization':f'Bearer {p}'})
    res1 = data1.json()
    res2 = data2.json()
    context={'data1': res1,'data2':res2} 
    return render(request,'his.html',context)

def acceptResource(request):
    id = request.GET['id']
    global p
    td=requests.get('https://sport-resources-booking-api.herokuapp.com/acceptResource',headers={'Authorization':f'Bearer {p}'},
    data={'id':id})
    res = td.json()
    return JsonResponse(res,safe=False)

def logout(request):
    return render(request,'logout.html')