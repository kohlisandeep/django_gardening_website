from django.shortcuts import render
from .models import Destination
# Create your views here.

def index(request):
    des1=Destination()
    des1.name='ginger'
    des1.plant='tulsi'
    des1.price=786
    des1.img='p1.jpg'
    des1.des='its testing 1'
    des1.offer=True

    des2=Destination()
    des2.name='coriander'
    des2.plant='papaya'
    des2.price=745
    des2.img='p2.jpg'
    des2.des='its testing 2'
    des2.offer=False

    des3=Destination()
    des3.name='chilli'
    des3.plant='banana'
    des3.price=123
    des3.img='p3.jpg'
    des3.des='its testing 3'
    des3.offer=True

    des4=Destination()
    des4.name='money'
    des4.plant='banayan'
    des4.price=489
    des4.img='p4.jpg'
    des4.des='its testing 4'
    des4.offer=False

    dest=[des1,des2,des3,des4]


    return render(request,'index.html',{'dest':dest})
