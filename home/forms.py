from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Details


class DetailsForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    class Meta: 
        model = Details
        #fields = '__all__'
        fields = ('name', 'mobile_num','age', 'address', 'department', 'email', 'password', 'confirm_password')
        labels = {
            'name': 'Full Name',
            'mobile_num': 'Phone Number',
        }
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    # def clean(self):
    #     cleaned_data = super(DetailsForm, self).clean()
    #     password = cleaned_data.get("password")
    #     confirm_password = cleaned_data.get("confirm_password")
    #     print(password, confirm_password)

    #     if password != confirm_password:
    #         raise forms.ValidationError(
    #             "password and confirm_password does not match"
    #         )

    def __init__(self, *args, **kwargs):
        super(DetailsForm,self).__init__(*args, **kwargs)
        self.fields['department'].empty_label = "Select Department"

    
