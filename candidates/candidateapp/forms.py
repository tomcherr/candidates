# from django import forms  
# from .models import Candidatedirectorys


from django import forms  
from candidateapp.models import Candidatedirectory
from django.forms import fields

class candidateForm(forms.ModelForm):  
    class Meta:  
        model = Candidatedirectory 
        fields = "__all__"  
