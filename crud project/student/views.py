from django.shortcuts import redirect, render
from .forms import StudentRegistration
from .models import User

def add_show(request):
    if request.method == 'POST':
        form = StudentRegistration(request.POST)
        if form.is_valid():
            form.save()
            #form = StudentRegistration()
            return redirect('addandshow')
    else:
        form = StudentRegistration()
    stud = User.objects.all()
    context = {'form':form,
                'stud': stud
              }
    return render(request, 'student/addandshow.html', context)

def delete_data(request, pk):
    if request.method == 'POST':
        obj = User.objects.get(id=pk)
        obj.delete()
        return redirect('addandshow')

def update_data(request, pk):
    if request.method == 'POST':
        obj = User.objects.get(id=pk)
        form = StudentRegistration(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('addandshow')
    else:
        obj = User.objects.get(id=pk)
        form = StudentRegistration(instance=obj)
    context = {'form': form}
    return render(request, 'student/updatestudent.html', context)
