from django.shortcuts import render, redirect
from .models import ItemList

# Create your views here.

def home(request):
	viewContent=request.POST.get('content')
	#viewDate=request.POST.get('taking_date')
	if request.method == 'POST' :
		dt=ItemList(content=viewContent)
		dt.save()
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
