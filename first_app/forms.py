from django import forms
from datetime import datetime
from .models import Inventory

YEARS = [x for x in range(1940,2050)]

class EmployeeForm(forms.Form):
    name = forms.CharField(label='Employee Name', max_length=100, widget=forms.TextInput(attrs={"style":"color:red",
                                                                                                "placeholder":"Enter your name "
                                                                                                }))
    birth_date = forms.DateField(label='Date of birth', widget=forms.SelectDateWidget(years=YEARS))
# TODO : HERE NAME IS TAKEN AS birth_date_month , how?
    salary = forms.IntegerField(label='salary')
    address = forms.CharField(label='Address', max_length=500, widget=forms.Textarea(attrs={'placeholder':'Enter Address'}))

# TODO: HOW TO ADD A BREAK HERE IN ATTRIBUTES
    # FOR INDIVIDUAL VALIDATION OR VALIDATION FOR ALL ATTRIBUTES WE USE CLEAN METHOD
    ''' TO VALIDATE ALL FIELDS IN THE FORM WE USE CLEAN() FUNCTION
        TO VALIDATE INDIVIDUAL ATTRIBUTES IN THE FORM WE USE clean_<fieldname>(): '''

    def clean_birth_date(self):
        birth_date = self.cleaned_data['birth_date']

        today = datetime.now().date()
        # CHECKING IF ENTERED BIRTH DATE IS EARLIER THAN TODAY.
        if birth_date > today:
            raise forms.ValidationError("Enter dates earlier than today", code="birth_date")

        if birth_date is None:
            raise forms.ValidationError(" ENTER THE BIRTH DATE",code='birth_date')
        return birth_date


    def clean_name(self):
        name = self.cleaned_data['name']
        if name == " ":
            raise forms.ValidationError("Enter a valid name", code="name")
        return name


class InventoryModelForm(forms.ModelForm):

    class Meta:
        model = Inventory
        fields = ('item', 'item_code', 'item_condition', 'quantity')

    def clean_item_code(self):
        item_code = self.cleaned_data['item_code']
        # emplist = Inventory.objects.all()
        # #emplist = list(emplist)
        # breakpoint()
        if item_code <= 0:
            raise forms.ValidationError("item code should be greater than zero", code=item_code)

        # for i in range(len(emplist)):
        #     for j in emplist[i]:
        #         if item_code == emplist[i].item_code:
        #             raise forms.ValidationError("Item code already mentioned, Enter new item code")
        item_code = str(item_code)
        if item_code.startswith("10"):
            pass
        else:
            raise forms.ValidationError("The item code should start with 10.")

        return item_code

    # defining a function to check wheather the item code starts with a digit or not
    # def clean_item_code(self):
    #     item_code = self.cleaned_data['item_code']
    #     item_code = str(item_code)
    #     if item_code.startswith("10"):
    #         pass
    #     else:
    #         raise forms.ValidationError("The item code should start with 10.")
    #     return

