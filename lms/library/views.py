from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Author,Book,Receiver,Transactionn
from .forms import Aform,Bform,Cform,Dform

# Create your views here.
def sample(s):
	return HttpResponse("tnr")

def home(request):
	return render(request,'tnr/home.html')
def author(request):
	d=Author.objects.all()
	if request.method=="POST":
		g=Aform(request.POST)
		if g.is_valid():
			g.save()
			return redirect('author')
	g=Aform()
	return render(request,'tnr/author.html',{'k':g,'e':d})
def Authordel(request,p):
	n=Author.objects.get(bookid=p)
	if request.method=="POST":
		n.delete()
		return redirect('author')
	return render(request,'tnr/authordel.html',{'Z':n})
def books(request):
	d=Book.objects.all()
	if request.method=="POST":
		g=Bform(request.POST)
		if g.is_valid():
			g.save()
			return redirect('book')
	g=Bform()
	return render(request,'tnr/books.html',{'k':g,'e':d})

def bookdel(request,l):
	b=Book.objects.get(authorid=l)
	if request.method=="POST":
		b.delete()
		return redirect("book")
	return render(request,"tnr/bookdel.html",{'z':b})
def receiver(request):
	a=Receiver.objects.all()
	if request.method=="POST":
		n=Cform(request.POST)
		if n.is_valid():
			n.save()
			return redirect("taken")
	n=Cform()
	return render(request,"tnr/receiver.html",{'k':n,'e':a})

def receiverdel(request,k):
	a=Receiver.objects.get(sid=k)
	if request.method=="POST":
		a.delete()
		return redirect("taken")
	return render(request,"tnr/receiverdel.html",{"z":a})

def transaction(request):
	a=Transactionn.objects.all()
	if request.method=="POST":
		n=Dform(request.POST)
		if n.is_valid():
			n.save()
			return redirect("trasaction")
	n=Dform()
	return render(request,"tnr/trasaction.html",{'k':n,'e':a})

def transdel(request,z):
	t=Transactionn.objects.get(transactionid=z)
	if request.method=="POST":
		t.delete()
		return redirect("trasaction")
	return render(request,"tnr/transactiondel.html",{"z":t})

