from django import forms
from .models import User
from argon2 import PasswordHasher, exceptions

class LoginForm(forms.Form):
    u_id = forms.CharField(
        max_length=32,
        label='id',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'u-id',
                'placeholder': 'id'
            }
        ),
        error_messages={'required': '아이디를 반드시 입력해주세요!'}

    )
    u_pw = forms.CharField(
        max_length=128,
        label='pw',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'u-pw',
                'placeholder': 'password'
            }
        ),
        error_messages={'required': '비밀번호를 반드시 입력해주세요!'}
    )

    field_order = [
        'u_id',
        'u_pw',
    ]

    def clean(self):
        cleaned_data = super().clean()

        u_id = cleaned_data.get('u_id', '')
        u_pw = cleaned_data.get('u_pw', '')

        if u_id =='':
            return self.add_error('u_id', '아이디를 반드시 입력해주세요.')
        elif u_pw == '':
            return self.add_error('u_pw', '비밀번호를 다시 입력해주세요.')
        else:
            try:
                user = User.objects.get(u_id=u_id)
            except User.DoesNotExist:
                return self.add_error('u_id','해당 아이디가 존재하지 않습니다.')

            try:
                PasswordHasher().verify(user.u_pw, u_pw)
            except exceptions.VerificationError:
                return self.add_error('u_pw', '비밀번호가 다릅니다.')


class RegisterForm(forms.ModelForm):
    u_id = forms.CharField(
        label='id',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'u-id',
                'placeholder': '아이디 입력'
            }
        ),
        error_messages={'required': '아이디를 입력해주세요!',
                        'unique' : '이미 존재하는 아이디입니다.'}
    )

    u_pw = forms.CharField(
        label='pw',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'u-pw',
                'placeholder': '비밀번호 입력'
            }
        ),
        error_messages={'required': '반드시 비밀번호를 입력해주세요!'}
    )

    u_pw_confirm = forms.CharField(
        label='re-pw',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'u-pw_confirm',
                'placeholder': '비밀번호 확인'
            }
        ),
        error_messages={'required': '비밀번호가 일치하지 않습니다!'}
    )

    u_name = forms.CharField(
        label='name',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'u-name',
                'placeholder': '사용할 이름 입력'
            }
        ),
        error_messages={'required': '반드시 사용할 이름을 입력해주세요!'}
    )

    u_phone = forms.CharField(
        label='phone',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'u-phone',
                'placeholder': '사용자 전화번호 입력'
            }
        ),
        error_messages={'required': '반드시 전화번호를 입력해주세요!',
                        'unique' : '이미 사용 중인 번호입니다.'}
    )

    field_order = [
        'u_id',
        'u_pw',
        'u_pw_confirm',
        'u_name',
        'u_phone'
    ]


    class Meta:
        model = User
        fields = [
            'u_id',
            'u_pw',
            'u_name',
            'u_phone'
        ]


    def clean(self):
        cleaned_data = super().clean()

        u_id = cleaned_data.get('u_id', '')
        u_pw = cleaned_data.get('u_pw', '')
        u_pw_confirm = cleaned_data.get('u_pw_confirm', '')
        u_name = cleaned_data.get('u_name', '')
        u_phone = cleaned_data.get('u_phone', '')

        if u_pw != u_pw_confirm:
            return self.add_error('u_pw_confirm', '비밀번호가 일치하지 않습니다!!')
        elif not (5 <= len(u_id) <= 20):
            return self.add_error('u_id', '아이디는 5~20자로 입력해주세요')
        elif 6 > len(u_pw):
            return self.add_error('u_pw', '보안을 위해 비밀번호는 6자 이상으로 적어주세요')
        else:
            self.u_id = u_id
            self.u_pw = PasswordHasher().hash(u_pw)
            self.u_pw_confirm = u_pw_confirm
            self.u_name = u_name
            self.u_phone = u_phone
