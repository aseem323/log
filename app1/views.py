from django.shortcuts import render

# Create your views here.
def testfn(request):
    return render(request,'login.html')

def test2fn(request):
    return render(request,'log2.html')