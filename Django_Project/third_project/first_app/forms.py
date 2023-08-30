from django import forms

class contactForm(forms.Form):
    name = forms.CharField(label='userName')
    email = forms.EmailField(label='userEmail')

    # age = forms.IntegerField()
    # weight = forms.FloatField()
    # blance = forms.DecimalField()
    # check = forms.BooleanField()
    # birthDay = forms.DateField()
    # appoinmnet = forms.DateTimeField()
    # CHOICES = [('S', 'Small'), ('M', 'Medium'), ('L', 'Large')]
    # szie = forms.ChoiceField(choices=CHOICES)
    # CHOICES = [('C', 'Chiken'), ('B', 'Beef'), ('M', 'Matton')]
    # pizza = forms.MultipleChoiceField(choices=CHOICES)

    file = forms.FileField()