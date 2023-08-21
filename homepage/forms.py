from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from homepage.models import *



class CreateUserform(UserCreationForm):
    class Meta:
        model= User
        fields = ["first_name", "last_name",'username','email','password1','password2','phone_number']

    def clean_email(self):
        email=self.cleaned_data.get("email")
        user_count= User.objects.filter(email=email).count()
        if user_count>0:
            raise forms.ValidationError("Already this email has been registered. Please try again.")
        return email

class PlaceSearchForm(forms.Form):
    min_price = forms.DecimalField(min_value=0.00)
    max_price = forms.DecimalField(min_value=0.00)

    def clean(self):
        cleaned_data = super().clean()
        min_price = cleaned_data.get('min_price')
        max_price = cleaned_data.get('max_price')

        if min_price is not None and max_price is not None:
            if min_price > max_price:
                raise forms.ValidationError("Minimum price must be less than or equal to the maximum price.")


class PackageBookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['number', 'persons', 'start_date', 'end_date']
        labels = {
            'number':'Enter Your Phone Number',
            'persons':'How Many Seat You need'
        }
        widgets = {
            'number':forms.NumberInput(attrs={'class':'form-control'}),
            'persons':forms.NumberInput(attrs={'class':'form-control'}),
            'start_date':forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
            'end_date':forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
        }

class AddPackageForm(forms.ModelForm):
    class Meta:
        model = Package
        fields = ['place','cover', 'name', 'source', 'destination','price', 'plan', 'terms']
        widgets = {
            'cover':forms.FileInput(attrs={'class':'form-control'}),
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'source':forms.TextInput(attrs={'class':'form-control'}),
            'destination':forms.TextInput(attrs={'class':'form-control'}),
            'plan':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Enter Your Plan'}),
            'terms':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Enter Terms and Conditions'}),
            'place':forms.Select(attrs={'class':'form-control'}),
            'price':forms.NumberInput(attrs={'class':'form-control'})
        }



class GuidesRegisterForm(forms.ModelForm):
    class Meta:
        model = Guide
        fields = ['place', 'name', 'age', 'photo', 'phone']

        widgets = {
            'place': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.TextInput(attrs={'class': 'form-control'}),
            'photo': forms.FileInput(attrs={'class': 'form-control-file'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
        }




class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = [ 'rating', 'comment']
        widgets = {
            'rating':forms.Select(attrs={'class':'form-control'}),
            'comment':forms.Textarea(attrs={'class':'form-control'}),
        }



class AddBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'video']

        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'video':forms.FileInput(attrs={'class':'form-control'})
        }