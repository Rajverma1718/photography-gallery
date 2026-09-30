from django import forms # type: ignore
from .models import Gallery

class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ['title', 'image', 'post']

        labels = {'title':'Title', 'image': 'Image', 'post':'Caption'}
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'title-control', 'placeholder': 'Enter title here'}),
            'post': forms.Textarea(attrs={'class': 'post-control', 'placeholder': 'Enter you caption here for the image'}),
            'image': forms.ClearableFileInput(attrs={'class': 'image-control'}),
        }

   