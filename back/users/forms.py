from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import QRUser


class QRUserCreationForm(UserCreationForm):

    class Meta:
        model = QRUser
        fields = ('username', )


class QRUserChangeForm(UserChangeForm):

    class Meta:
        model = QRUser
        fields = ('username', )
