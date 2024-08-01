from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label="username", max_length=200)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

class SignUpForm(forms.Form):
    username = forms.CharField(
        label="Username",
        max_length=50,
        min_length=5,
        required=True,
        initial="Enter your username",
        help_text="enter your username here",
        widget=forms.Textarea(attrs={
            'placeholder': 'Username'
            }),
        error_messages={'required': 'This field is required.', 
                        'max_length': 'Maximum length is 50 characters.'
                        }
        )


    first_name = forms.CharField(
        label="Username",
        max_length=50,
        required=True,
          )
    second_name = forms.CharField(
        label="Username",
          max_length=50,
          required=True,
          )
    password = forms.CharField(
        label="Password",  
        widget=forms.PasswordInput,
        help_text="enter a strong password",
        required=True
        )
    confirm_password = forms.CharField(
     label="Confirm password",
      widget=forms.PasswordInput,
      help_text="enter a strong password",
      required=True
      )
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match")