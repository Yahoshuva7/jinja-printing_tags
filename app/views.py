from django.shortcuts import render

# Create your views here.
def Send(request):
    d={'name':'Yahoshuva','Age':9}
    return render(request,'send_data.html',context=d)