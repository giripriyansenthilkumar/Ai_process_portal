from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django import forms
from .models import Registration, FamilyDetails, Applicant, BankDetails  # Ensure all models are imported
import json

# Define the registration form
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

# Define the applicant form
class ApplicantForm(forms.Form):
    full_name = forms.CharField(max_length=150, required=True)
    mobile_number = forms.CharField(max_length=10, required=True)
    email = forms.EmailField(required=True)
    dob = forms.DateField(required=True)
    country = forms.CharField(max_length=100, required=True)
    state = forms.CharField(max_length=100, required=True)
    city = forms.CharField(max_length=100, required=True)

# Define the family details form
class FamilyDetailsForm(forms.Form):
    applicant_email = forms.EmailField(required=True)
    father_name = forms.CharField(max_length=150, required=True)
    father_dob = forms.DateField(required=True)
    father_phone = forms.CharField(max_length=10, required=True)
    father_email = forms.EmailField(required=True)
    father_occupation = forms.CharField(max_length=150, required=True)
    father_employer = forms.CharField(max_length=150, required=True)
    father_income = forms.FloatField(required=True)
    father_education = forms.CharField(max_length=150, required=True)
    mother_name = forms.CharField(max_length=150, required=True)
    mother_dob = forms.DateField(required=True)
    mother_phone = forms.CharField(max_length=10, required=True)
    mother_email = forms.EmailField(required=True)
    mother_occupation = forms.CharField(max_length=150, required=True)
    mother_employer = forms.CharField(max_length=150, required=True)
    mother_income = forms.FloatField(required=True)
    mother_education = forms.CharField(max_length=150, required=True)
    father_itr = forms.FileField(required=False)
    father_bank_statements = forms.FileField(required=False)
    father_assets = forms.FileField(required=False)
    existing_loans = forms.CharField(max_length=150, required=False)
    guarantor_name = forms.CharField(max_length=150, required=False)
    guarantor_relation = forms.CharField(max_length=150, required=False)
    guarantor_occupation = forms.CharField(max_length=150, required=False)
    guarantor_income = forms.FloatField(required=False)
    guarantor_itr = forms.FileField(required=False)
    guarantor_bank_statements = forms.FileField(required=False)

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

def home(request):
    return render(request, 'aippapp/home.html')

def login_view(request):
    return render(request, 'aippapp/login.html')

def register(request):
    form = RegistrationForm()
    return render(request, 'aippapp/reg.html', {'form': form})

@csrf_exempt
def register_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            try:
                registration = Registration(
                    email=form.cleaned_data['email'],
                    phone=form.cleaned_data['phone'],
                    username=form.cleaned_data['username'],
                    dob=form.cleaned_data['dob'],
                    password=form.cleaned_data['password']
                )
                registration.save()
                return redirect('success')  # Redirect to the success view
            except Exception as e:
                return JsonResponse({'errors': str(e)}, status=500)
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    else:
        return JsonResponse({'message': 'Invalid request method. Only POST is allowed.'}, status=405)

@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')

        try:
            user = Registration.objects.get(username=username, password=password)
            return JsonResponse({'success': True})
        except Registration.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Invalid credentials'})
    else:
        return JsonResponse({'message': 'Invalid request method. Only POST is allowed.'}, status=405)

def success(request):
    return render(request, 'aippapp/success.html')

def app1(request):
    form = ApplicantForm()
    return render(request, 'aippapp/app1.html', {'form': form})

@csrf_exempt
def save_applicant(request):
    if request.method == 'POST':
        form = ApplicantForm(request.POST)
        if form.is_valid():
            try:
                applicant = Applicant(
                    full_name=form.cleaned_data['full_name'],
                    mobile_number=form.cleaned_data['mobile_number'],
                    email=form.cleaned_data['email'],
                    dob=form.cleaned_data['dob'],
                    country=form.cleaned_data['country'],
                    state=form.cleaned_data['state'],
                    city=form.cleaned_data['city']
                )
                applicant.save()
                return redirect('app2')  # Redirect to the success view
            except Exception as e:
                return JsonResponse({'errors': str(e)}, status=500)
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    else:
        return JsonResponse({'message': 'Invalid request method. Only POST is allowed.'}, status=405)

def app2(request):
    form = FamilyDetailsForm()
    return render(request, 'aippapp/app2.html', {'form': form})

@csrf_exempt
def save_family_details(request):
    if request.method == 'POST':
        form = FamilyDetailsForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                family_details = FamilyDetails(
                    applicant_email=form.cleaned_data['applicant_email'],
                    father_name=form.cleaned_data['father_name'],
                    father_dob=form.cleaned_data['father_dob'],
                    father_phone=form.cleaned_data['father_phone'],
                    father_email=form.cleaned_data['father_email'],
                    father_occupation=form.cleaned_data['father_occupation'],
                    father_employer=form.cleaned_data['father_employer'],
                    father_income=form.cleaned_data['father_income'],
                    father_education=form.cleaned_data['father_education'],
                    mother_name=form.cleaned_data['mother_name'],
                    mother_dob=form.cleaned_data['mother_dob'],
                    mother_phone=form.cleaned_data['mother_phone'],
                    mother_email=form.cleaned_data['mother_email'],
                    mother_occupation=form.cleaned_data['mother_occupation'],
                    mother_employer=form.cleaned_data['mother_employer'],
                    mother_income=form.cleaned_data['mother_income'],
                    mother_education=form.cleaned_data['mother_education'],
                    father_itr=form.cleaned_data.get('father_itr'),
                    father_bank_statements=form.cleaned_data.get('father_bank_statements'),
                    father_assets=form.cleaned_data.get('father_assets'),
                    existing_loans=form.cleaned_data.get('existing_loans'),
                    guarantor_name=form.cleaned_data.get('guarantor_name'),
                    guarantor_relation=form.cleaned_data.get('guarantor_relation'),
                    guarantor_occupation=form.cleaned_data.get('guarantor_occupation'),
                    guarantor_income=form.cleaned_data.get('guarantor_income'),
                    guarantor_itr=form.cleaned_data.get('guarantor_itr'),
                    guarantor_bank_statements=form.cleaned_data.get('guarantor_bank_statements')
                )
                family_details.save()
                return redirect('app3')  # Redirect to the success view
            except Exception as e:
                return JsonResponse({'errors': str(e)}, status=500)
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    else:
        return JsonResponse({'message': 'Invalid request method. Only POST is allowed.'}, status=405)

def app3(request):
    form = BankDetailsForm()
    return render(request, 'aippapp/app3.html', {'form': form})

@csrf_exempt
def save_bank_details(request):
    if request.method == 'POST':
        form = BankDetailsForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                bank_details = BankDetails(
                    account_number=form.cleaned_data['account_number'],
                    bank_name=form.cleaned_data['bank_name'],
                    account_type=form.cleaned_data['account_type'],
                    ifsc_code=form.cleaned_data['ifsc_code'],
                    branch_name=form.cleaned_data['branch_name'],
                    aadhar_number=form.cleaned_data['aadhar_number'],
                    bank_statements=form.cleaned_data.get('bank_statements'),
                    loan_account=form.cleaned_data.get('loan_account'),
                    monthly_income=form.cleaned_data['monthly_income'],
                    other_income_sources=form.cleaned_data.get('other_income_sources')
                )
                bank_details.save()
                print("Bank details saved successfully!")
                return redirect('success')  # Redirect to the success view
            except Exception as e:
                print(f"Error saving bank details: {e}")
                return JsonResponse({'errors': str(e)}, status=500)
        else:
            print("Form is not valid:", form.errors)
            return JsonResponse({'errors': form.errors}, status=400)
    else:
        return JsonResponse({'message': 'Invalid request method. Only POST is allowed.'}, status=405)

def app4(request):
    return render(request, 'aippapp/app4.html')
