from django.shortcuts import render
from friends.forms import CreateNewCategory, CreateNewFriend
from friends.models import Category, Info
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def info(request):
    friends_list = Info.objects.order_by('-id')
    return render(request, 'info.html', {'friends_list':friends_list})

def category_list(request):
    category_list = Category.objects.order_by('id')
    return render(request, 'category_list.html', {'category_list':category_list})
def add_category(request):
    form = CreateNewCategory()
    if request.method == 'POST':
        form = CreateNewCategory(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return HttpResponse("You added a new category successfully!")
        else:
            print("ERROR FORM INVALID!!!")
    return render(request, 'create_category.html', {'form': form})
def add_friend(request):
    form = CreateNewFriend()
    if request.method == 'POST':
        form = CreateNewFriend(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return info(request)
        else:
            print("ERROR FORM INVALID!!!")
    return render(request, 'create_friend.html', {'form':form})
