from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
import datetime
from django.forms.extras.widgets import SelectDateWidget
from registration.models import Person
from django.views.decorators.csrf import csrf_protect
from django.core.context_processors import csrf

year = datetime.date.today().year

class RegisterUser(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "password1", "password2", "first_name", "last_name", "email")

class RegisterPerson(ModelForm):
    class Meta:
        model = Person
        fields = ("birthday", "mobilenum", "fromuser")
        widgets = {
            "birthday": SelectDateWidget(years=range(year, year - 101, -1), required=False)
        }

class Birthday(ModelForm):
    class Meta:
        model = Person
        fields = ("birthday",)
        widgets = { "birthday": SelectDateWidget(years=range(year, year - 101, -1), required=False) }