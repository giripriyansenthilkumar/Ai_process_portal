from django import forms

class RegistrationForm(forms.Form):
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=15, required=True)
    username = forms.CharField(max_length=150, required=True)
    dob = forms.DateField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    confirm_password = forms.CharField(widget=forms.PasswordInput, required=True)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Password and Confirm Password do not match.")

class BankDetailsForm(forms.Form):
    account_number = forms.CharField(max_length=18, required=True)
    bank_name = forms.CharField(max_length=150, required=True)
    account_type = forms.ChoiceField(choices=[('savings', 'Savings'), ('current', 'Current'), ('salary', 'Salary')], required=True)
    ifsc_code = forms.CharField(max_length=11, required=True)
    branch_name = forms.CharField(max_length=150, required=True)
    aadhar_number = forms.CharField(max_length=12, required=True)
    bank_statements = forms.FileField(required=False)
    loan_account = forms.CharField(max_length=18, required=False)
    monthly_income = forms.FloatField(required=True)
    other_income_sources = forms.CharField(max_length=500, required=False, widget=forms.Textarea)
