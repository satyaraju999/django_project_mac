from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=50,null=False)
    description = models.CharField(max_length=50,null=False)
    date_created = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(null=True)

    def __str__(self):
        return f"{self.name} - {self.description}"


class Employee(models.Model):
    name = models.CharField(max_length=50,null=False)
    dob = models.DateField(null=False)
    salary = models.IntegerField(null=False)
    address = models.CharField(max_length=200, null=False)
    date_created = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

class Areas(models.Model):
    areaname = models.CharField(max_length=50 , null=False)
    areamember = models.CharField(max_length=100, null=False,default='satya')
    areacode = models.IntegerField(null=False)
    areadistrict = models.CharField(max_length=20, default='HYD')


class Book(models.Model):
    number_of_trades: models.IntegerField(null=False)
    profit_trades = models.IntegerField(null=False)
    loss_trades = models.IntegerField(null=False)
    date_of_trade = models.DateField(null=False)