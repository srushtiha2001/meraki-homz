from django import forms
from .models import Comment





class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = [
			'content'

		]



class ContactForm(forms.Form):
    subject = forms.CharField()
    from_email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea , required=True)