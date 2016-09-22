from django import forms

class AddForm(forms.Form):
    company_code = forms.CharField(label='Company Code',max_length=150, required=True, widget=forms.TextInput(attrs={'placeholder':'Please enter company code'}))
    target_price = forms.FloatField(label='Target Price',required=True, widget=forms.TextInput(attrs={'placeholder':'123.45'}))