from django import forms

class regform(forms.Form):
    username = forms.CharField(max_length=25)
    phone=forms.IntegerField()
    psw = forms.CharField(max_length=20)


class logform(forms.Form):
    phone = forms.IntegerField()
    psw = forms.CharField(max_length=20)