# from django import forms  
# from .models import Candidatedirectorys

# class CandidateForm(forms.ModelForm):
#     class Meta:
#         model = Candidatedirectorys
#         fields = '__all__'  
#         exclude = ['status', 'created_date', 'created_by', 'modified_date', 'modified_by']
from django import forms  
from candidateapp.models import Candidatedirectory
from django.forms import fields

class candidateForm(forms.ModelForm):  
    class Meta:  
        model = Candidatedirectory 
        fields = "__all__"  
