from django.shortcuts import render, redirect
from django.http import HttpResponse
from RoanList.models import Item

def MainPage(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST['newEntry1'])
        return redirect('/')
    #return render(request,'mainpage.html')
    items = Item.objects.all()
    return render(request,'mainpage.html') #, {'newPerson': items})

# Create your views here.
#def MainPage(request):
	#return render(request,'mainpage.html',{'newPerson':request.POST.get('newEntry1'),'newPlace':request.POST.get('newPlace1',''),})

#def MainPage(request):
#    if request.method == 'POST':
#        newItem = request.POST['newEntry1']
#        Item.objects.create(text=newItem)
#    else:
#        newItem = ' '
#    return render(request,'mainpage.html',{'newPerson': newItem,})
    
    #item1 = Item()
    #item1.text=request.POST.get('newEntry1', ' ')
    #item1.save()
    #return render(request,'mainpage.html',{'newPerson':item1.text,})   
    
    
    
