from django import forms

from news.models import News
from news.validators import check_to_number


class NewsForm(forms.Form):
    title = forms.CharField(label='Title ',
                            max_length=100,
                            widget=forms.TextInput(attrs={'class': 'form-control'}),
                            validators=[check_to_number, ])
    overview = forms.CharField(label="Overview",
                               widget=forms.Textarea(attrs={'class': 'form-control'}))
    body = forms.CharField(label="Body",
                           widget=forms.Textarea(attrs={'class': 'form-control'}))


class NewsModelForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'overview', 'body']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'label': 'Title'})
        }
