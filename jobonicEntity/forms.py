from django import forms


class LoginForm(forms.Form):
    first_name = forms.CharField(label='First name', max_length=50, help_text='Your first name')
    last_name = forms.CharField(label='Last name', max_length=50, help_text='Your last name')
    pc_email = forms.EmailField(label='Company Email', max_length=70, help_text='Your Company Email')
    pc_phone = forms.CharField(label='Company Phone', max_length=11, help_text='Phone number we can reach you on')
    comp_name = forms.CharField(label='Company Name', max_length=30, help_text='Company Name')
    website = forms.URLField(label='Company Website', max_length=30, help_text='Company Website')
    password = forms.CharField(widget=forms.PasswordInput(), label='Password', max_length=30, help_text='Your Password')
    conf_password = forms.CharField(widget=forms.PasswordInput(), label='Confirm Password', max_length=30, help_text='Confirm Password')
