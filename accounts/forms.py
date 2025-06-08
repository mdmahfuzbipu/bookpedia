from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AdminUserCreationForm, UserCreationForm, UserChangeForm

# For frontend signup
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = (
            "email",
            "username",
        )


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = (
            "email",
            "username",
        )

# For Django Admin
class CustomAdminUserCreationForm(AdminUserCreationForm):
    class Meta:
        model = get_user_model()
        fields = (
            "email",
            "username",
        )

