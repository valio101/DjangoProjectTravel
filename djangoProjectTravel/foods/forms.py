from django import forms

from djangoProjectTravel.foods.models import Food


class FoodBaseForm(forms.ModelForm):
    class Meta:
        model = Food
        exclude = ('publication_date', 'user', )


class PhotoCreateForm(FoodBaseForm):
    pass


class FoodEditForm(FoodBaseForm):
    class Meta:
        model = Food
        exclude = ('publication_date', )


class FoodDeleteForm(FoodBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__disable_fields()

    def __disable_fields(self):
        for name, field in self.fields.items():
            # field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        else:
            pass
        return self.instance

