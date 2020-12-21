from django.forms import ModelForm
from .models import Student, Course, Category
from django import forms


class StudentRegistrationForm(ModelForm):
    def __int__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.updates({'class':'form-control'})

    class Meta:
        model = Student
        fields = '__all__'
        widgets = {
            'registrationDate':forms.DateInput(attrs={'type':'date','class':'datepicker'})
        }