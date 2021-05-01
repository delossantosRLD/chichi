from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.
def MainPage(request):
	return render(request,'mainpage.html',{'newPerson':request.POST.get('NewEntry1'),'newPlace':request.POST.get('newPlace1',''),})
    #pass
    
