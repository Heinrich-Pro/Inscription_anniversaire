from django.shortcuts import render, redirect
from inscriptions.models import Participant
from .forms import ParticipantForm

def inscription_view(request):
    if request.method == 'POST':
        form = ParticipantForm(request.POST)
        if form.is_valid():
            participant = form.save()

            return redirect('confirmation')
    else:
        form = ParticipantForm()
    return render(request, 'inscription.html', {'form': form})

def confirmation_view(request):
    return render(request, 'confirmation.html')

from django.contrib.auth.decorators import login_required

@login_required
def liste_participants_view(request):
    participants = Participant.objects.all()
    return render(request, 'liste_participants.html', {'participants': participants})

