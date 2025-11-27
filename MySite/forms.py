from django import forms


class userForms(forms.Form):
    num1=forms.CharField(label="value1",required=False,widget=forms.TextInput(attrs={'class':"form-control"}))
    num2=forms.CharField(label="value2",required=False,widget=forms.TextInput(attrs={'class':"form-control"}))
    num3=forms.CharField(label="value3",required=False,widget=forms.TextInput(attrs={'class':"form-control"}))
    # email=forms.EmailField()
    ch1=forms.ChoiceField()



class marksheetForm(forms.Form):
    subject1=forms.CharField()
    subject2=forms.CharField()
    subject3=forms.CharField()
    subject4=forms.CharField()
    subject5=forms.CharField()    