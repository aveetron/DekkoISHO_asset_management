from django import forms
#from django.forms import ModelForm
from itequp.models import *


class SupplierForms(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = '__all__'


class CompanyForms(forms.ModelForm):
    class Meta:
        model = CompanyMaster
        fields = '__all__'


class DepartmentForms(forms.ModelForm):
    class Meta:
        model = DepartmentMaster
        fields = '__all__'



class DeviceTypeForms(forms.ModelForm):
    class Meta:
        model = DeviceType
        fields = '__all__'



class AllocateDeviceForm(forms.ModelForm):
    class Meta:
        model = AllocateDevice
        fields = '__all__'