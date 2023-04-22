from django import forms
from photos.models.photo import Photo


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = {'photo', 'signature'}
        labels = {
            'photo': 'Картинка',
            'signature': 'Подпись',
        }


class SearchForm(forms.Form):
    search = forms.CharField(max_length=20, required=False, label='Найти')


class FavoriteForm(forms.Form):
    note = forms.CharField(max_length=30, required=False, label='Заметка')
