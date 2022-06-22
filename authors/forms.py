from click import password_option
from django import forms
from django.contrib.auth.models import User


def add_attr(field, attr_name, attr_new_val):
    existing = field.widget.attrs.get(attr_name, '')
    field.widget.attrs[attr_name] = f'{existing} {attr_new_val}'.strip()


def add_placeholder(field, placeholder_val):
    add_attr(field, 'placeholder', placeholder_val)


class RegisterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_placeholder(self.fields['username'], 'Your username2')
        add_placeholder(self.fields['email'], 'Your e-mail')
        add_placeholder(self.fields['first_name'], 'Ex.: John')
        add_placeholder(self.fields['last_name'], 'Ex.: Doe')
        add_attr(self.fields['username'], 'css', 'a-css-class')

    # sobrescrever campo
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Your password'
        }),
        error_messages={
            'required': 'Password must not be empty'
        },
        help_text=(
            'Password must have at least ondeuppercase letter, '
            'one lowercase letter and one number.'
        )
    )

    # criando novo campo
    password2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Repeat your password'
        })
    )

    class Meta:
        model = User
        # fields = '__all__'
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
        ]

        labels = {
            'first_name': 'First name',
            'last_name': 'Last name',
            'username': 'User-name',
            'email': 'E-mail',
            'password': 'Passwword',
        }

        help_texts = {
            'email': 'The e-mail must be valid',
        }

        error_messages = {
            'username': {
                'required': 'The field must not be empty',
            }
        }

        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'Type your first name here.',
            }),

            'last_name': forms.TextInput(attrs={
                'placeholder': 'Type your last name here.',
            }),

            'password': forms.PasswordInput(attrs={
                'placeholder': 'Type your password here',
            })
        }

    # método para validar um campo

    # def clean_password(self):
    #     data = self.cleaned_data.get('password')
    #     if 'atenção' in data:
    #         raise forms.ValidationError(
    #             'Não digite %(erro)s no campo password',
    #             code='ivalid',
    #             params={'erro': '"atenção"'}
    #         )
    #     return data

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError(
                'Password and password2 must be equal'
            )
