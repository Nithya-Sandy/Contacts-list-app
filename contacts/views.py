from django.http.response import HttpResponse
from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import Contact
import re
# from tkinter import messagebox 

# Create your views here.

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

def index(request):
    contacts = Contact.objects.all()
    search_input = request.GET.get('search-area')
    if search_input:
        contacts = Contact.objects.filter(full_name__icontains=search_input)
    else:
        contacts = Contact.objects.all()
        search_input = ''
    return render(request, 'index.html', {'contacts': contacts, 'search_input': search_input})


def addContact(request):
    if request.method == 'POST':
        name=request.POST['fullname']
        rel=request.POST['relationship']
        mail=request.POST['email']
        phone=request.POST['phone-number']
        add=request.POST['address']
        if(re.fullmatch(regex, mail) and len(phone)==10):
            new_contact = Contact(full_name=name,relationship=rel,email=mail,phone_number=phone,address=add)
            new_contact.save()
        else:
            return HttpResponse("Enter valid email and Phone_number should be of length 10.")
        # else:
        #     messagebox.showerror('Validation Error', 'Email should be in the format name@gmail.com')
        #     return redirect('/add-contact')
        return redirect('/')
    return render(request, 'new.html')


def editContact(request, pk):
    contact = Contact.objects.get(id=pk)
    if request.method == 'POST':
        name = request.POST['fullname']
        rel = request.POST['relationship']
        mail = request.POST['email']
        phone = request.POST['phone-number']
        add = request.POST['address']
        if(re.fullmatch(regex, mail) and len(phone)==10):
            contact.full_name = name
            contact.relationship = rel
            contact.email = mail
            contact.phone_number = phone
            contact.address = add
            contact.save()
        else:
            return HttpResponse("Enter valid email or Phone_number should be of length 10.")
        return redirect('/profile/'+str(contact.id))
    return render(request, 'edit.html', {'contact': contact})


def deleteContact(request, pk):
    contact = Contact.objects.get(id=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('/')
    return render(request, 'delete.html', {'contact': contact})


def contactProfile(request, pk):
    contact = Contact.objects.get(id=pk)
    return render(request, 'contact-profile.html', {'contact':contact})