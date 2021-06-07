from django.forms import ModelForm
from . models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
		
class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields =['username','email','password1','password2']



class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields= ('customer','number','company_name','name','car_number','location','image','image1','image2','Year','g','Km','des', 'Owners','totalprice')
        labels  = {
        'customer':'Your name ', 
        'number':'Phone number', 
        'name':'Car Model name ', 
        'location':'Location', 
        'image':' Primary Picture',
        'image1':' 2nd Picture',
        'image2':' 3rd Picture',

        'g':'In Gurantee or Not',
        'Year':'Year of Manufacturing',
        'Km':'Km in used',
        'des':'Description',
        'car_number':'First 4 digit of car_number',
        'Owners':'Number of Pervious Owners',
        'totalprice':'Price expecting',
        }

        widgets = {

        'Year': forms.NumberInput(attrs={'class':'form-control'}),
        'number': forms.TextInput(attrs={'class':'form-control'}),
        'location': forms.TextInput(attrs={'class':'form-control'}),
        'Year': forms.TextInput(attrs={'class':'form-control'}),
        'Owners': forms.NumberInput(attrs={'class':'form-control'}),
        'name': forms.TextInput(attrs={'class':'form-control'}),
        'price': forms.NumberInput(attrs={'class':'form-control'}),
        'Km': forms.NumberInput(attrs={'class':'form-control'}),
        'des': forms.Textarea(attrs={'class':'textarea','row':10,'cols':50}),
        'customer': forms.TextInput(attrs={'class':'form-control'}),
        
        }

class CreateblogForm(forms.ModelForm):
    class Meta:
        model = blog
        fields =['Title','image','des','au']
        labels  = {
        'au':'Author_Name', 
        'des':'Description', 
        'image':'Picture',
    
        }
        widgets = {
        'des': forms.Textarea(attrs={'class':'textarea','row':10,'cols':50}), 
             
            }
            
class ViewForm(forms.ModelForm):
    class Meta:
        model = Product
        fields= ('customer','number','company_name','name','car_number','location','image','Year','g','Km','des', 'Owners','totalprice')
        labels  = {
        'customer':'Your name ', 
        'number':'Phone number', 
        'name':'Car Model name ', 
        'location':'Location', 
        'image':' Primary Picture',
        'g':'In Gurantee or Not',
        'Year':'Year of Manufacturing',
        'Km':'Km in used',
        'des':'Description',
        'car_number':'First 4 digit of car_number',
        'Owners':'Number of Pervious Owners',
        'totalprice':'Price expecting',
        }

        widgets = {

        'Year': forms.NumberInput(attrs={'class':'form-control'}),
        'number': forms.TextInput(attrs={'class':'form-control'}),
        'location': forms.TextInput(attrs={'class':'form-control'}),
        'Year': forms.TextInput(attrs={'class':'form-control'}),
        'Owners': forms.NumberInput(attrs={'class':'form-control'}),
        'name': forms.TextInput(attrs={'class':'form-control'}),
        'price': forms.NumberInput(attrs={'class':'form-control'}),
        'Km': forms.NumberInput(attrs={'class':'form-control'}),
        'des': forms.Textarea(attrs={'class':'textarea','row':10,'cols':50}),
        'customer': forms.TextInput(attrs={'class':'form-control'}),
        
        }
