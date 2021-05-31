from allauth.account.forms import LoginForm


class CustomLoginForm(LoginForm):

    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)
        self.fields['login'].widget.attrs.update({
            'class': 'login-email-field'
        })
        self.fields['password'].widget.attrs.update({
            'class': 'login-password-field'
        })
