from myforum.models import Themes, ForumMessages, IconSmiles
from django.forms import ModelForm
from django.forms import widgets
from django import forms

class NewTheme(ModelForm):
    class Meta:
        model = Themes
        fields = ("nametheme", "themetext")

class NewMessage(ModelForm):
    class Meta:
        model = ForumMessages
        fields = ("messtext", )

class NSmile(ModelForm):
    class Meta:
        model = IconSmiles
        fields = ("smileicon", "smileview")
#        widgets = {"smileicon": forms.FileInput}

'''class NSmile(forms.Form):
    smileicon = forms.ImageField(widget=forms.ClearableFileInput)
    smileview = forms.CharField(max_length=10)'''