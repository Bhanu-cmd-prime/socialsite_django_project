from django.shortcuts import render

# Create your views here.
def index(request):
    contex_dict={'text':'helloworld','number':100}
    return render(request,'basicapp/index.html',context=contex_dict)

def other(request):
    return render(request,'basicapp/other.html')

def relative(request):
    return render(request,'basicapp/relative.html')

def base(request):
    return render(request,'basicapp/base.html')