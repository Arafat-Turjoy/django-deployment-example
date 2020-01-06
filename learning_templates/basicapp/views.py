from django.shortcuts import render

# Create your views here.
def index(request):
    context_dict = {'text':'Hello World','number':100}
    return render(request,'basicapp/index.html',context_dict)

def relative_url(request):
    return render(request,'basicapp/relative_url.html')

def others(request):
    return render(request,'basicapp/others.html')
