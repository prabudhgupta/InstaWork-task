from django import forms
from .models import user_form,User
# creating a form
class InputForm(forms.Form):
 
    ROLE = [('R','Regular'),('A','Admin')]
    
    role=forms.CharField(label='ROLE', widget=forms.RadioSelect(choices=ROLE), initial={
        'R':'Regular'
    })

class InputmodelForm(forms.ModelForm):
    ROLE = [('R','Regular'),('A','Admin')]
    role=forms.CharField(label='ROLE', widget=forms.RadioSelect(choices=ROLE), initial={'R':'Regular'})

    
    '''def clean_email(self):
        email = self.cleaned_data['email']
        qs = user_form.objects.filter(email=email)
        if self.instance.pk is not None:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError("There is already an user with email: %s" % email)'''
    
    class Meta:
        model = user_form
        fields =  "__all__"  