from django.shortcuts import render
from itequp.forms import *
from django.http import HttpResponseRedirect
from itequp.models import *
from django.contrib import messages



# Create your views here.
def supplier(request):
    allSupplier = Supplier.objects.all()
    context = {
        'allSupplier': allSupplier
    }
    return render(request, 'supplier.html', context)


def addSupplier(request):
    if request.method == 'POST':
        request.POST = request.POST.copy()
        if Supplier.objects.filter(name = request.POST['name']).exists():
            print('this supplier already exists!')
            message = 'this supplier already exists!'
            messages.warning(request, message)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            request.POST['created_by'] = 1
            request.POST['status'] = True
            forms = SupplierForms(request.POST)
            if forms.is_valid():
                forms.save()
                message = 'supplier added successfully'
                messages.success(request, message)
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            else:
                print('forms is not valid')
                message = 'forms is not valid'
                messages.warning(request, message)
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        print('not a post message')
        message = 'not possible'
        messages.warning(request, message)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    


def company(request):
    allCompany = CompanyMaster.objects.all()
    context = {
        'allCompany': allCompany
    }
    return render(request, 'company.html', context)


def addCompany(request):
    if request.method == 'POST':
        request.POST = request.POST.copy()
        if CompanyMaster.objects.filter(name = request.POST['name']).exists():
            print('this supplier already exists!')
            message = 'this company already exists!'
            messages.warning(request, message)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            request.POST['created_by'] = 1
            request.POST['status'] = True
            forms = CompanyForms(request.POST)
            if forms.is_valid():
                forms.save()
                message = 'Company added successfully'
                messages.success(request, message)
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            else:
                print('forms is not valid')
                message = 'forms is not valid'
                messages.warning(request, message)
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        print('not a post message')
        message = 'not possible'
        messages.warning(request, message)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def department(request):
    allDepartment = DepartmentMaster.objects.all()
    context = {
        'allDepartment': allDepartment
    }
    return render(request, 'department.html', context)


def addDepartment(request):
    if request.method == 'POST':
        request.POST = request.POST.copy()
        if DepartmentMaster.objects.filter(name = request.POST['name']).exists():
            print('this supplier already exists!')
            message = 'this department already exists!'
            messages.warning(request, message)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            request.POST['created_by'] = 1
            request.POST['status'] = True
            forms = DepartmentForms(request.POST)
            if forms.is_valid():
                forms.save()
                message = 'supplier added successfully'
                messages.success(request, message)
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            else:
                print('forms is not valid')
                message = 'forms is not valid'
                messages.warning(request, message)
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        print('not a post message')
        message = 'not possible'
        messages.warning(request, message)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def deviceType(request):
    allDeviceType = DeviceType.objects.all()
    context = {
        'allDeviceType': allDeviceType
    }
    return render(request, 'deviceType.html', context)


def addDeviceType(request):
    if request.method == 'POST':
        request.POST = request.POST.copy()
        if DeviceType.objects.filter(name = request.POST['name']).exists():
            print('this supplier already exists!')
            message = 'this supplier already exists!'
            messages.warning(request, message)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            request.POST['created_by'] = 1
            request.POST['status'] = True
            forms = DeviceTypeForms(request.POST)
            if forms.is_valid():
                forms.save()
                message = 'supplier added successfully'
                messages.success(request, message)
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            else:
                print('forms is not valid')
                message = 'forms is not valid'
                messages.warning(request, message)
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        print('not a post message')
        message = 'not possible'
        messages.warning(request, message)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))




def allocateDevice(request):
    allEmployee = Employee.objects.all()
    allDeviceType = DeviceType.objects.all()
    allDeviceAllocate = AllocateDevice.objects.all()
    allSupplier = Supplier.objects.all()
    context = {
        'allEmployee': allEmployee,
        'allDeviceType': allDeviceType,
        'allDeviceAllocate': allDeviceAllocate,
        'allSupplier': allSupplier
    }
    return render(request, 'allocateDevice.html', context)




def addAllocationDevice(request):
    if request.method == 'POST':
        request.POST = request.POST.copy()
        request.POST['created_by'] = 1
        request.POST['status'] = True
        forms = AllocateDeviceForm(request.POST)
        if forms.is_valid():
            forms.save()
            message = 'Allocated successfully'
            messages.success(request, message)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            print('forms is not valid')
            message = 'forms is not valid'
            messages.warning(request, message)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        print('not a post message')
        message = 'not possible'
        messages.warning(request, message)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
