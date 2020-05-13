'''
Created on Apr 13, 2020

@author: shamim
'''

from django.forms.models import ModelForm
from student.models import Student
from django.forms.widgets import TextInput, Select, DateInput, EmailInput,\
    NumberInput, Textarea
from django import forms


GENDER_CHOICES= [
    ('male', 'MALE'),
    ('female', 'FEMALE'),
    ('others', 'OTHER'),
    ]
GROUP_CHOICES= [
    ('science', 'SCIENCE'),
    ('humanities', 'HUMANITIES'),
    ('commerce', 'COMMERCE'),
    ]
FACALTY_CHOICES= [
    ('as', 'APPLIED SCIENCE'),
    ('ps', 'PHYSICAL SCIENCE'),
    ('ls', 'LIFE SCIENCE'),
    ('ss','SOCIAL SCIENCE'),
    ('bba','BUSINESS FACALTY'),
    ]
class DateInput(forms.DateInput):
    input_type='date'
class StudentForm(ModelForm):
    class Meta:
        model=Student
        exclude= ('department',)
        widgets = {
            'first_name': TextInput(attrs={'placeholder': 'FIRST NAME'}),
            'last_name': TextInput(attrs={'placeholder': 'LAST NAME'}),
            'gender': Select(attrs={'placeholder': 'GENDER'}, choices=GENDER_CHOICES),
            'date_of_birth': DateInput(),
            'fathers_name': TextInput(attrs={'placeholder': 'FATHERS NAME'}),
            'mothers_name': TextInput(attrs={'placeholder': 'MOTHERS NAME'}),
            'email': EmailInput(attrs={'placeholder': 'EMAIL'}),
            'phone': NumberInput(attrs={'placeholder': 'PHONE'}),
            'hsc_gpa': NumberInput(attrs={'placeholder': 'HSC GPA', 'step': '0.01'}),
            'ssc_gpa': NumberInput(attrs={'placeholder': 'SSC GPA', 'step': '0.01'}),
            'group': Select(attrs={'placeholder': 'GROUP'}, choices=GROUP_CHOICES),
            'unit': Select(attrs={'placeholder': 'FACALTY'}, choices= FACALTY_CHOICES),
            'address': Textarea(attrs={'placeholder': 'Write your present address', 'rows':2, 'cols':15}),
        }
    
    def is_valid(self):
        valid = super(StudentForm,self).is_valid()
        if not valid:
            return valid
        group=self.cleaned_data['group']
        unit=self.cleaned_data['unit']
        if group== "science" and (unit=="as" or unit=="ls" or unit=="ps"):
            return valid
        elif group=="humanities" and unit=="ss":
            return valid
        elif group=="commerce" and unit=="bba":
            return valid
        else:
            msg="Group and Facalty must match"
            self.add_error('group', msg)
               
        return valid 
    
        
        
       
    
        
        
