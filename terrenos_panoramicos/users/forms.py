from django import forms


class ProfileForm(forms.Form):
    """Profile form."""

    curp = forms.CharField(max_length=18,required=True )
    phone_number = forms.CharField(max_length=20, required=False)
    picture = forms.ImageField()
    ine = picture = forms.ImageField()