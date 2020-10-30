from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'index.html')

def submitquery(request):
    q=request.GET['query']
    try:
        ans=eval(q)
        md={
            "q":q,
            "ans":ans,
            "error":False,
            "answer":True
        }
        print(ans)
        return render(request,'index.html',context=md)

    except:
        md={
            "error":True,
            "answer":False
        }
        return render(request,'index.html',context=md)
   