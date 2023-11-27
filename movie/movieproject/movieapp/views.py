from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import MovieForm
from . models import Movie
# Create your views here.
def demo(request):
    obj=Movie.objects.all()
    abc={
        'movie_list':obj,
         }
    return render(request,'index.html',abc)


def details(request,movie_id):
    film=Movie.objects.get(id=movie_id)
    return render(request,'details.html',{'movie':film})

def add(request):
    if request.method=="POST":
        name=request.POST.get('name')
        dese = request.POST.get('dese')
        year = request.POST.get('year')
        img = request.FILES['img']
        movie=Movie(name=name,dese=dese,year=year,img=img)

        movie.save()

        return redirect('/')

    return render(request,'add.html')

def update(request,id):
    movie=Movie.objects.get(id=id)
    form=MovieForm(request.POST or None, request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')

    return render(request,'edit.html',{'movie':movie,'form':form})


def delete(request,id):
    if request.method=='POST':
        movie=Movie.objects.get(id=id)
        movie.delete()

        return redirect('/')

    return render(request,'delete.html')