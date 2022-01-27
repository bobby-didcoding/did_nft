from django import forms

class NFTForm(forms.Form):
	
	quantity = forms.IntegerField(required=True,
		widget=forms.NumberInput(attrs={
			'placeholder': '*Quantity..',
			'class': 'form-control'
			}))
	class Meta:
		fields = ('quantity',)