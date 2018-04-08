from django import forms



class IpForm(forms.Form):
    ip = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Enter an IP Address', 'size':48}))