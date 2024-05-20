from django.shortcuts import render , redirect ,get_object_or_404

from app1.forms import formView
from .models import*


def page1(request):
    tree = book.objects.all()
    context = {'tree' : tree}
    return render(request , "date.html" , context )


def page2(request , id):
    tree = book.objects.get(id = id)
    context = {'tree' : tree}
    return render(request , "next.html" , context )

def forming(request):
    data = {'form1' : formView()}
    return render(request , "form_value.html" , data)



def adddata(request):
    x = request.POST['name']
    y = request.POST['rollNo']
    z = request.POST['department']

    tree = book(name = x , rollNo = y , department = z)

    tree.save()

    return redirect("/")

def delete(request , id):
    tree = book.objects.get(id = id)

    tree.delete()

    return redirect("/")
def update(request ,id):
    context = {}
    obj = get_object_or_404(book, id = id)
    data = formView(request.POST or None,instance=obj)
    if data.is_valid():
        data.save()
        return redirect('/')
    context['form'] = data
    return render(request , "update.html" , context)