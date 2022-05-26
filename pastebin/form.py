from django import forms


class PasteForm(forms.Form):
    content = forms.CharField(label='content')


class CodeForm(forms.Form):
    title = forms.CharField(label='title')
