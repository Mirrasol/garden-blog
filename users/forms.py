from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


class UserForm(UserCreationForm):
    """
    A custom User form based on UserCreationForm.
    """
    usable_password = None

    class Meta:
        model = get_user_model()
        fields = [
            'first_name',
            'last_name',
            'username',
            'password1',
            'password2',
        ]

    def clean_username(self):
        return self.cleaned_data.get('username')
