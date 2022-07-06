from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def HomeView(request):
    return render(request,'home.html')
def HomeInput(request):
    firstname=request.GET['t1']
    lastname=request.GET['t2']
    mobileno=int(request.GET['t3'])
    return HttpResponse("succussful registration")
#basic registration format
#def home(request):
#


