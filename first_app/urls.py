from django.urls import path
from .views import home
from .views import about, news, get_dept_details, get_area_details, get_employee_details, sign_in, sign_up, create_depatment, dept_list

urlpatterns = [
    path('home/', home, name='home'),
    path('about/', about, name='about'),
    path('news/', news),
    path("departments/<int:dept_id>/", get_dept_details),
    path("areas/<int:area_id>/", get_area_details),
    path("employee/<int:emp_id>/", get_employee_details),
    path("sign_in/", sign_in),
    path("sign_up/", sign_up),
    path("department/create_department/", create_depatment, name='create_department'),
    path("department/dept_list/", dept_list, name='dept_list'),
]