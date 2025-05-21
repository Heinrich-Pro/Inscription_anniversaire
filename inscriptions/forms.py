from django import forms
from .models import Participant

class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['nom', 'email', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 4}),
        }
