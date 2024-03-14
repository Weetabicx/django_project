class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = UserFormfields = ('username', 'email', 'password',)

    class UserProfileForm(forms.ModelForm):
        class Meta:
            model = UserProfile
            fields = ('website', 'picture',)