from tokenize import Name
from django.shortcuts import render
from django.views import View
from .models import Element
from .forms import CustomerProfileForm
from django.contrib import messages

class ElementView(View):
    def get(self,request):
        element=Element.objects.all()
        return render(request,'main3.html',{'element':element})
         

class ElementDetail(View):
    def get(self,request,pk):
        product1=Element.objects.get(pk=pk)
        element=Element.objects.all()
        return render(request,'main3.html',{'element':element,'product1':product1})

class ProfileView(View):
    def get(self,request):
        element=Element.objects.all()
        form = CustomerProfileForm()
        return render(request,'main3.html',{'element':element,'form':form})
    
    def post(self,request):
        form=CustomerProfileForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['Name']
            text=form.cleaned_data['Text']
            reg=Element(Name=name,Text=text)
            reg.save()
            messages.success(request,'Congratulations! New Element added Successfully')
        return render(request,'main3.html')