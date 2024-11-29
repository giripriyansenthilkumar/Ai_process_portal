from mongoengine import Document, fields
from django import forms

class Applicant(Document):
    meta = {'collection': 'applicants_details'}
    full_name = fields.StringField(required=True)
    mobile_number = fields.StringField(required=True, max_length=10)
    email = fields.EmailField(required=True)
    dob = fields.DateField(required=True)
    country = fields.StringField(required=True)
    state = fields.StringField(required=True)
    city = fields.StringField(required=True)

    def __str__(self):
        return self.full_name

class Registration(Document):
    meta = {'collection': 'registrations'}
    email = fields.EmailField(required=True, unique=True)
    phone = fields.StringField(max_length=15, required=True)
    username = fields.StringField(max_length=150, required=True, unique=True)
    dob = fields.DateField(required=True)
    password = fields.StringField(max_length=128, required=True)

    def __str__(self):
        return self.username

class FamilyDetails(Document):
    meta = {'collection': 'family_details'}
    applicant_email = fields.EmailField(required=True)
    father_name = fields.StringField(required=True)
    father_dob = fields.DateField(required=True)
    father_phone = fields.StringField(max_length=10, required=True)
    father_email = fields.EmailField(required=True)
    father_occupation = fields.StringField(required=True)
    father_employer = fields.StringField(required=True)
    father_income = fields.FloatField(required=True)
    father_education = fields.StringField(required=True)
    mother_name = fields.StringField(required=True)
    mother_dob = fields.DateField(required=True)
    mother_phone = fields.StringField(max_length=10, required=True)
    mother_email = fields.EmailField(required=True)
    mother_occupation = fields.StringField(required=True)
    mother_employer = fields.StringField(required=True)
    mother_income = fields.FloatField(required=True)
    mother_education = fields.StringField(required=True)
    father_itr = fields.FileField(required=False)
    father_bank_statements = fields.FileField(required=False)
    father_assets = fields.FileField(required=False)
    existing_loans = fields.StringField(required=False)
    guarantor_name = fields.StringField(required=False)
    guarantor_relation = fields.StringField(required=False)
    guarantor_occupation = fields.StringField(required=False)
    guarantor_income = fields.FloatField(required=False)
    guarantor_itr = fields.FileField(required=False)
    guarantor_bank_statements = fields.FileField(required=False)

    def __str__(self):
        return self.applicant_email

class BankDetails(Document):
    meta = {'collection': 'bank_details'}
    account_number = fields.StringField(required=True)
    bank_name = fields.StringField(required=True)
    account_type = fields.StringField(required=True)
    ifsc_code = fields.StringField(required=True)
    branch_name = fields.StringField(required=True)
    aadhar_number = fields.StringField(required=True)
    bank_statements = fields.FileField(required=False)
    loan_account = fields.StringField(required=False)
    monthly_income = fields.FloatField(required=True)
    other_income_sources = fields.StringField(required=False)

    def __str__(self):
        return self.account_number

