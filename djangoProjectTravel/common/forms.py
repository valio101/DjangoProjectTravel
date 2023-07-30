from django import forms

from djangoProjectTravel.common.models import PhotoComment


class PhotoCommentForm(forms.ModelForm):
    class Meta:
        model = PhotoComment
        fields = ('text', )
        widgets = {
            'text': forms.Textarea(
                attrs={
                    'cols': 40,
                    'rows': 10,
                    'placeholder': 'Add comment...'
                },
            ),
        }


class SearchPhotosForm(forms.Form):
    search_by_destination_name = forms.CharField(max_length=50, required=False, )