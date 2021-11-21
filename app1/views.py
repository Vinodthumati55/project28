from django.shortcuts import render

# Create your views here.
def jinja(request):
    d={'name':'ganesh'}
    return render(request,'h1.html',context=d)
def jinja1(request):
    d={'a':15,'b':20,'c':25}
    return render(request,'h2.html',context=d)