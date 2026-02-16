from django.shortcuts import render

from django.http import HttpResponse

def home(request):


    peoples = [
        {'name' :'Abhijeet Gupta' , 'age':26},
        {'name' :'timble' , 'age':27},
        {'name' :'glance Gupta' , 'age':28},
        {'name' :'ai Gupta' , 'age':29}
    ]

    return render(request , "index.html" , context={'peoples':peoples})


def success_page(request):
    print("*" * 10)
    return HttpResponse("<h1>hey i am Success Page</h1>")
