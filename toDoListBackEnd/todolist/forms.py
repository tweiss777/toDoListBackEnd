from django import forms
from django.core.validators import RegexValidator

class ExistingUserForm(forms.Form):
    reg = r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$"           
    email = forms.CharField(required=True,validators=[RegexValidator(reg,"Invalid email supplied")])
    password = forms.CharField(required=True)



class NewUserForm(forms.Form):
    reg = r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$" 
    
    first_name = forms.CharField(max_length=50,required=True)
    last_name = forms.CharField(required=True,max_length=50)
    email = forms.CharField(required=True,validators=[RegexValidator(reg,"Invalid email supplied")])
    password = forms.CharField(required=True)

    

