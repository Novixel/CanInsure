from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NewUserForm(UserCreationForm):
    user_id = forms.IntegerField(required=True)
    first_name = forms.CharField(required=True, max_length=200)
    last_name = forms.CharField(required=True, max_length=200)
    date_of_birth = forms.DateField(required=True, widget=forms.TextInput(attrs={'type': 'date'} ))
    address = forms.CharField(required=True, max_length=255)
    phone = forms.IntegerField(required=True, min_value=10)
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ("user_id", "username", "first_name", "last_name", "date_of_birth", "address", "phone", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.user_id = self.cleaned_data['user_id']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.dob = self.cleaned_data['date_of_birth']
        user.address = self.cleaned_data['address']
        user.phone = self.cleaned_data['phone']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user 