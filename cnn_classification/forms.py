from django import forms

class ImageUploadForm(forms.Form):

    imagen = forms.ImageField(widget=forms.FileInput(attrs={'class':'file', 'type':'file', 'data-browse-on-zone-click': 'true'}))