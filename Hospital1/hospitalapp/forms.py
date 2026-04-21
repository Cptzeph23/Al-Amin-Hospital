
from Hospital1.hospitalapp.models import Contact


def ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']    


def emailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = ['email']