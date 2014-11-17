from django.shortcuts import render


# Create your views here.
def index(request):
	
	return render(request,'index.html',{'range': range(4)})

def inscribete(request):
	return render(request, 'inscribete.html') 