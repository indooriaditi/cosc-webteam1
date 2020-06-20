from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
# from .models import Question
import requests

p=''
# Create your views here.
def index(request):
    #data=Question.objects.order_by('-pub_date')[:5]
    #context={
        #'question_list':data
    #}
    #return render(request, 'index.html', context)
    return ''

def detail(request,question_id):
    return HttpResponse("You are lokking at question %s" % question_id)

def api_call(request):
    token = requests.post("https://sport-resources-booking-api.herokuapp.com/login",data={'id': '160118733012','password':'abc123'} )
    global p
    p = token.json()['access_token']
    data = requests.get("https://sport-resources-booking-api.herokuapp.com/ResourcesPresent", headers = {'Authorization':f'Bearer {p}'}) 
    res = data.json()
    context={'data': res,} 
    return render(request,'api.html',context)
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
    global p
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

