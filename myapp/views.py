from django.shortcuts import render,HttpResponse,get_list_or_404, get_object_or_404
from myapp.models import Ignis


# Create your views here.
def index(request):
    ignis=Ignis.objects.all()
    mod=Ignis()
    print(ignis)
    n=len(ignis)
    #print(ignis[0].is_liked)  True
    params={'n':n,'ignis':ignis,'range':range(1,n+1)}
    if request.method=="POST":
        
        heart=request.POST.get('heart')
        print(heart)
        if heart=="on":
            mod.is_liked=True
        else:
            mod.is_liked=False
        mod.save()
        
    

       


    return render(request,'myapp/index.html',params)
