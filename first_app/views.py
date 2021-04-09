from django.shortcuts import render, HttpResponse, redirect
from .models import  Department, Areas, Employee, Inventory
from .forms import EmployeeForm, InventoryModelForm

def home(request):
    return render(request, 'first_app/home.html', context={'fullname': 'satya raju kusampudi'})


def about(request):
    return render(request, 'first_app/about.html')

def news(request):
    return render(request, 'first_app/news.html')


def get_dept_details(request, dept_id):
    print(" ID is ",dept_id)
    # select * from department where id = dept_id
    try:
        dept_details = Department.objects.get(pk = dept_id)
    except Exception as e:
        dept_details= None

    dept = { }
    if dept_details :
        dept['name'] = dept_details.name
        dept['description'] = dept_details.description
    else:
        dept['exception'] = f"NO Details found for id {dept_id}"
    import json
    return render(request,template_name="first_app/dept_details.html",context=dept)

def get_area_details(request,area_id):
    try:
        area_details = Areas.objects.get(pk = area_id)
    except Exception as e:
        area_details = None

    area = { }
    if area_details:
        area['areaname'] = area_details.areaname
        area['areacode'] = area_details.areacode
        area['areamember'] = area_details.areamember
    else:
        area['Exception'] = f" NO Area found with that  {area_id} Code"
    return render(request,template_name="first_app/areas.html",context=area)

def get_employee_details(request, emp_id):
    try:
        emp_details = Employee.objects.get(pk=emp_id)
    except Exception as e:
        emp_details = None

    emp = {}
    if emp_details:
        emp['name'] = emp_details.name
        emp['dob'] = emp_details.dob
        emp['salary'] = emp_details.salary
        emp['address'] = emp_details.address
        emp['date_created'] = emp_details.date_created
        emp['date_updated'] = emp_details.date_updated
        emp['department'] = emp_details.department
    else:
        emp['exception'] = f" No employee with {emp_id} id"
    return render(request,template_name="first_app/employee.html",context=emp)

def sign_in(request):
    return render(request,template_name="first_app/sign_in.html",context={})

def sign_up(requset):
    return render(requset,template_name="first_app/sign_up.html",context={})

def create_depatment(request):

    if request.method == 'GET':
        return render(request, template_name="first_app/create_department.html", context={})

    elif request.method == 'POST':
        dept_name = request.POST['deptName']
        dept_description = request.POST['description']
        # location = request.POST['location']
        # pin_code = request.POST['pinCode']
        dept = Department(name=dept_name, description=dept_description)
        #dept = Department(name=dept_name, description= dept_description, location=location, pincode=pin_code)
        dept.save()
        return redirect(to='dept_list')

def dept_list(request):
    departments = Department.objects.all()
    context = {}
    # PASSING DEPARTMENTS TO CONTEXT , AND USING THE SAME departments in HTML TO RENDER IN THE WEBPAGE
    context['departments'] = departments
    return render(request, template_name="first_app/dept_list.html", context=context)


def render_with_django_form(request):
    context = {}
    if request.method == 'GET':
        #
        form = EmployeeForm()
        context['employeeForm'] = form
        return render(request, template_name='first_app/login_form.html', context=context)

    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        context['employeeForm'] = form
        if form.is_valid():
            emp_name = form.cleaned_data['name']
            emp_dob = form.cleaned_data['birth_date']
            emp_salary = form.cleaned_data['salary']
            emp_address = form.cleaned_data['address']
            department= Department.objects.get(pk=2)

            emp1 = Employee(name=emp_name, dob=emp_dob, salary=emp_salary, address=emp_address, department=department)
            emp1.save()
            return redirect(to='emp_list')
        else:
            return render(request, template_name='first_app/login_form.html', context=context)

def emp_list(request):
    employees = Employee.objects.all()
    context = {}
    context['employees'] = employees

    return render(request, template_name='first_app/emp_list.html',context=context)

def inventory_view(request):
    context = {}
    context['inventoryForm'] = InventoryModelForm()
    if request.method == 'GET':
        return render(request,template_name='first_app/inventory.html', context=context)
    elif request.method == 'POST':
        form = InventoryModelForm(request.POST)
        context['inventoryForm'] = form

        if form.is_valid():
            form.save()

            return redirect(to='inventory_list')
        else:
            return render(request, template_name='first_app/inventory.html',context=context)
def inventory_list(request):
    inventory = Inventory.objects.all()
    context= {}
    context['inventory'] = inventory

    return render(request, template_name='first_app/inventory_list.html', context= context)








    # # GIVING EMPTY CONTEXT, IS USED FOR DYNAMIC DATA LOADING TO WEB PAGE
    # context = {}
    #
    # # CHECKING WHEATHER THE METHOD IS POST OR GET, TO SEND DATA SAFE IN POST, OR GET(TO RETRIEVE THE HTML FORM)
    # if request.method == 'POST':
    #     # CAPTURING THE EmployeeForm class from forms.py , and using request.POST to capture the client data for intial validation
    #     # Server side
    #     # mapping EmployeeForm to variable form
    #     form = EmployeeForm(request.POST)
    #     context['employeeForm'] = form
    #
    #     # is_valid() is used for server side validation using forms, cleans
    #     if form.is_valid():
    #         return HttpResponse("Form submitted sucessfully")
    #
    #
    # else:
    #     form = EmployeeForm()
    #     context['employeeForm'] = form
    #
    # return render(request, template_name="first_app/login_form.html", context=context)

# DOUBT : GET AND POST METHODS , DO WE HAVE CALL GET METHOD TO OPEN THE PAGE