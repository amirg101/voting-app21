from django.shortcuts import render
arr=['Java','Python','C++','C','DotNet','JavaScript','PHP','Swift','SQL','MATLAB','Go','VisualBasic','Perl','R','D','Assemblylanguage','Ruby']
globalcount= dict()
# Create your views here.

from django.http import HttpResponse
def index(request):
    myd={
        "arr":arr
    }
    return render(request,'index.html',context=myd)

def getquery(request):
    q=request.GET['languages']
    if q in globalcount:
        globalcount[q]=globalcount[q]+1
    else:
        globalcount[q]=1
    myd={
        "arr":arr,
        "globalcount":globalcount
    }
    return render(request,'index.html',context=myd)

def sortdata(request):
    global globalcount
    globalcount=dict(sorted(globalcount.items(),key=lambda x:x[1],reverse=True)) 
    myd={
        "arr":arr,
        "globalcount":globalcount
    }
    return render(request,'index.html',context=myd)
