from django.shortcuts import render, redirect
from django.http import HttpResponse

from todo.models import Task
from todo.forms import *

#Create your views here.

def index(request):
	alltasks = Task.objects.all()
	form = TaskForm()

	if(request.method == "POST"):
		form = TaskForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect("/")

	context = {"alltasks":alltasks,"form":form}
	return render(request,"list.html",context)

def update_task(request,pk):
	task = Task.objects.get(id=pk)
	form = TaskForm(instance=task)
	if(request.method == "POST"):
		form = TaskForm(request.POST,instance=task)
		if form.is_valid():
			form.save()
			return redirect("/")
	context = {"task":task,"form":form}
	return render(request,"update_task.html",context)

def delete_task(request,pk):
	task = Task.objects.get(id=pk)
	if(request.method == "POST"):
		print("one")
		task.delete()
		print("two")
		return redirect("/")
	context = {"task":task}
	return render(request,"delete_task.html",context)