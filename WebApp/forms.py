from django import forms
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
# from django.forms import fields
from .models import *

class CountryForm(forms.ModelForm):
    
    class Meta:
        model=Country
        fields= ["name"]

class StateForm(forms.ModelForm):
    
    class Meta:
        model=State
        fields= ['state_name', 'country']

class CityForm(forms.ModelForm):
    
    class Meta:
        model=City
        fields= ['city_name', 'country', 'state']

# State
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        if 'country' in self.data:
            print('fghd')
            try:
                country_id = int(self.data.get('country'))
                self.fields['state'].queryset = State.objects.filter(
                    country = country_id).order_by('country')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk and self.instance.country:
            self.fields['state'].queryset = self.instance.country.state_set.order_by(
                'state_name')
        else:
            self.fields['state'].queryset = State.objects.all()

    # # City
    #     self.fields['city'].queryset = City.objects.none()

    #     if 'state' in self.data:
    #         try:
    #             state_id = int(self.data.get('state'))
    #             self.fields['city'].queryset = City.objects.filter(
    #                 state_id=state_id).order_by('name')
    #         except (ValueError, TypeError):
    #             pass
    #     elif self.instance.pk and self.instance.state:
    #         self.fields['city'].queryset = self.instance.state.city_set.order_by(
    #             'name')

    # # Street
    #     self.fields['street'].queryset = State.objects.none()

    #     if 'city' in self.data:
    #         try:
    #             city_id = int(self.data.get('city'))
    #             self.fields['street'].queryset = Street.objects.filter(
    #                 city_id=city_id).order_by('name')
    #         except (ValueError, TypeError):
    #             pass
    #     elif self.instance.pk and self.instance.city:
    #         self.fields['street'].queryset = self.instance.city.street_set.order_by(
    #             'name')







class CategoryForm(forms.ModelForm):
    
    class Meta:
        model=Category
        fields= ['name']

class UrlForm(forms.ModelForm):
    class Meta:
        model=Url
        fields = ['country', 'state', 'city', 'category', 'url' ]

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()
    def handle_uploaded_file(f):
        with open('some/file/name.txt', 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)

class ImageForm(forms.ModelForm):

    class Meta:
        model=UploadImage
        fields =['Image']

class PhoneForm(forms.ModelForm):
    class Meta:
        model=Details
        fields = ['name', 'whatsapp' ]