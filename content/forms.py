from django import forms
from django.forms.models import inlineformset_factory
from .models import Story
from accounts.models import UserAccount


class StoryForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = (
            'title',
            'content',
            'live'
        )


StoryFormSet = inlineformset_factory(
    UserAccount,
    Story,
    form=StoryForm,
    min_num=1,  # minimum number of forms that must be filled in
    extra=0,  # number of empty forms to display
    can_delete=False  # show a checkbox in each form to delete the row
)