from django.shortcuts import render

# Create your views here.
def testfn(request):
    return render(request,'login.html')