from django import forms
from .models import Activity, Donation


class EventForm(forms.ModelForm):
        class Meta:
                model = Activity
                fields = ['activity_name', 'activity_description', 'activity_start_date', 'activity_end_date', 'activity_picture', 'activity_type']
                widgets = {
                        'activity_name': forms.TextInput(attrs={'class':'form-control'}),
                        'activity_description': forms.TextInput(attrs={'class':'form-control', 'rows': 3}),
                        'activity_start_date': forms.SelectDateWidget(attrs={'class':'form-control', 'cols': '1'}),
                        'activity_end_date': forms.SelectDateWidget(attrs={'class':'form-control'}),
                        'activity_picture': forms.FileInput(attrs={'class': 'form-control'}),
                        'activity_type': forms.Select(attrs={'class': 'form-control'}),
                }
                exclude = ("user",)



class DonationForm(forms.ModelForm):
        class Meta:
                model = Donation
                fields = ['donation_name','donation_type', 'donation_description']
                widgets = {
                        'donation_type': forms.Select(attrs={'class': 'form-control'}),
                        'donation_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
                        'donation_name': forms.TextInput(attrs={'class': 'form-control', 'value': ""})
                }
                exclude = ("activity",)


class ContributionForm(forms.Form):
        name = forms.CharField(widget= forms.TextInput(attrs={'class':'form-control'}), label='Nombre')
        message = forms.CharField(widget= forms.Textarea(attrs={'class':'form-control'}), label='Mensaje')
        phoneNumber = forms.CharField(widget= forms.TextInput(attrs={'class':'form-control'}), label='Telefono con lada')
        sender = forms.EmailField(widget= forms.TextInput(attrs={'class':'form-control'}), label='Correo')

