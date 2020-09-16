from django.db import models

# Create your models here.
class Supplier(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    created_by = models.IntegerField()
    created_date = models.DateField(auto_now=True)
    status = models.BooleanField(default=1)

    def __str__(self):
        return self.name
    


class CompanyMaster(models.Model):
    name = models.CharField(max_length=30)
    short_name = models.CharField(max_length=20)
    created_by = models.IntegerField()
    created = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

# mode for department


class DepartmentMaster(models.Model):
    name = models.CharField(max_length=50)
    created_by = models.IntegerField()
    created = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name



class DeviceType(models.Model):
    name = models.CharField(max_length=50)
    created_by = models.IntegerField()
    created = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=100)
    employee_id = models.CharField(max_length=50)
    company = models.ForeignKey(CompanyMaster, on_delete=models.CASCADE)
    department = models.ForeignKey(DepartmentMaster, on_delete=models.CASCADE)



class AllocateDevice(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    device_type = models.ForeignKey(DeviceType, on_delete=models.CASCADE)
    model = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    qty = models.IntegerField(default=0)
    purchase_date = models.DateField(auto_now=False)
    assign_date = models.DateField(auto_now=False)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    serial_number = models.CharField(max_length=50)
    remarks = models.CharField(max_length=100)
    created_by = models.IntegerField()
    created = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    