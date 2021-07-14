from django.shortcuts import render, redirect
from .models import ItemList
from django.contrib import messages

# Create your views here.

def home(request):
	viewContent=request.POST.get('content')
	#viewDate=request.POST.get('taking_date')
	if request.method == 'POST' :
		dt=ItemList(content=viewContent)
		dt.save()
		messages.success(request,'Successfully Saved')
		return redirect('/') #To solved 'reload and automatically add' problem
	documents=ItemList.objects.all().order_by('taking_date')

	context={
		'documents' : documents,
	}
	return render(request, 'index.html',context)

def delete_item(request, tid):
	document=ItemList.objects.get(id=tid)
	document.delete()
	print('deleted', tid)
	#return render(request, 'index.html')
	return redirect('/')

def edit(request, tid):
	document=ItemList.objects.get(id=tid)
	context={
		'document':document,
	}
	if request.method == 'POST':
		contentField=request.POST.get('content') #.get('htmlfield name')
		dt=ItemList(content=contentField, id=tid)
		dt.save()
		messages.success(request,'Successfully Edited')
		print(contentField)
		return redirect('/')
	return render(request, 'edit.html', context)
	
