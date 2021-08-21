from django import forms
from django.forms.forms import Form
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Agent, Lead
from .forms import  LeadModelForm

# Create your views here.

def landing_page(request):
    return render(request, "landing.html")



def lead_list(request):
    leads = Lead.objects.all()
    context = {
        "leads":leads,
    }
    return render(request, 'leads/lead_list.html',context)

def lead_detail(request,pk):
    
    lead = Lead.objects.get(id=pk)
    context = {
        "lead": lead,
    }
    return render(request, 'leads/lead_detail.html',context)

def lead_create(request):
    # print(request.POST)
    form = LeadModelForm()
    if request.method == "POST":
        
        form = LeadModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/leads")
    context = {
        "form":LeadModelForm()
    }
    return render(request,"leads/lead_create.html",context)


def lead_update(request,pk):
    lead = Lead.objects.get(id = pk)
    form = LeadModelForm(instance=lead)
    if request.method == "POST":
        form = LeadModelForm(request.POST, instance= lead)
        if form.is_valid():
            form.save()
            return redirect("/leads")

    context = {
        "lead" : lead,
        "form" : form,
    }
    return render(request,"leads/lead_update.html",context)


def lead_delete(request,pk):
    lead = Lead.objects.get(id = pk)
    lead.delete()
    return redirect("/leads")


# def lead_update(request,pk):
#     lead = Lead.objects.get(id = pk)
#     form = LeadModelForm()
#     if request.method == "POST":
#         form = LeadModelForm(request.POST)
#         if form.is_valid():
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             age = form.cleaned_data['age']
            
#             lead.first_name = first_name
#             lead.last_name = last_name
#             lead.age = age
#             lead.save()

#             return redirect("/leads")
#     context = {
#         "lead": lead,
#         "form" : form
#     }

#     return render(request,"leads/lead_update.html",context)


# def lead_create(request):
#     # print(request.POST)
    # form = LeadModelForm()
    # if request.method == "POST":
    #     print("Receiving a Post request")
    #     form = LeadModelForm(request.POST)
    #     if form.is_valid():
    #         # print("The Form is Valid")
    #         # print(form.cleaned_data)
    #         # first_name = form.cleaned_data['first_name']
    #         # last_name = form.cleaned_data['last_name']
    #         # age = form.cleaned_data['age']
    #         # agent = form.cleaned_data['agent']
    #         # Lead.objects.create(
    #         #     first_name = first_name,
    #         #     last_name = last_name,
    #         #     age = age,
    #         #     agent = agent,
    #         # )
    #         # print("The Lead has been created")
    #         return redirect("/leads")
#     context = {
#         "form":LeadModelForm()
#     }
#     return render(request,"leads/lead_create.html",context)