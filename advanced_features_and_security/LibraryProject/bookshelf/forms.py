from django import forms

class BookSearchForm(forms.Form):
    title = forms.CharField(max_length=100)

class ExampleForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)