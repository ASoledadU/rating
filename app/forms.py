from django import forms


class AddForm(forms.Form):
    x = forms.IntegerField()
    y = forms.IntegerField()


class AddForms(forms.Form):
    points = forms.IntegerField()
