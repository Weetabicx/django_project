from django import forms
from django.contrib.auth.models import User


class UserEditForm(forms.ModelForm):
    bio = forms.CharField(widget=forms.Textarea, required=False)
    phone = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
        super(UserEditForm, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['bio'].initial = self.instance.userprofile.bio
            self.fields['phone'].initial = self.instance.userprofile.phone

    def save(self, commit=True):
        user = super(UserEditForm, self).save(commit=commit)
        user.userprofile.bio = self.cleaned_data['bio']
        user.userprofile.phone = self.cleaned_data['phone']
        if commit:
            user.userprofile.save()
        return user
