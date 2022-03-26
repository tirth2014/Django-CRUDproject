from django.shortcuts import render, redirect
from myapp1.forms import StudentForm
from .models import Student


def insertData(request):
    form = StudentForm
    return render(request, 'helloworld.html', {'form': form})


def add(request):
    form = StudentForm(request.POST)
    form.save()
    return redirect('/show')


def show(request):
    student = Student.objects.all()
    return render(request, "show.html", {'student': student})


def delete(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('/show')


def update(request, id):
    student = Student.objects.get(id=id)
    form = StudentForm(request.POST, instance=student)
    form.save()
    return redirect('/show')

def edit(request, id):
    student = Student.objects.get(id=id)
    return render(request, 'edit.html', {'student': student})