from django.shortcuts import render
from django.http import HttpResponseRedirect


def index_view(request):

    name = request.GET.get('name', 'John')
    age = request.GET.get('age', '18')

    context = {
        'name': name,
        'age': int(age)
    }

    return render(request, 'index.html', context)

def about_view(request):
    return render(request, 'about.html')

def task1_view(request):
    return render(request, 'task1.html')

def task3_view(request):
    return render(request, 'task3.html')


def task2_view(request):
    return render(request, 'task2.html')

def task6_view(request):
    return render(request, 'task6.html')


def article_create_view(request):
    if request.method == "GET":
        return render(request, 'article_create.html')
    elif request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        author = request.POST.get('author')
        context = {
            'title': title,
            'content': content,
            'author': author
        }
        # return HttpResponseRedirect('/')
        return render(request, 'article_new.html', context)
