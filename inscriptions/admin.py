from django.contrib import admin
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.http import HttpResponseRedirect
from django.urls import path
from .models import Participant

@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('nom', 'email', 'message')
    search_fields = ('nom', 'email')
    list_filter = ('nom',)
    actions = ['send_confirmation_email']

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('send-confirmation-email/<int:participant_id>/', self.admin_site.admin_view(self.send_confirmation_email_view), name='send_confirmation_email'),
        ]
        return custom_urls + urls

    def send_confirmation_email(self, request, queryset):
        # Action pour envoyer un email à plusieurs participants sélectionnés
        for participant in queryset:
            message = render_to_string('email_confirmation.txt', {'participant': participant})
            send_mail(
                'Confirmation d\'inscription',
                message,
                settings.DEFAULT_FROM_EMAIL,
                [participant.email],
                fail_silently=False,
            )
        self.message_user(request, f"{queryset.count()} email(s) de confirmation envoyé(s) avec succès.")

    send_confirmation_email.short_description = "Envoyer un email de confirmation"

    def send_confirmation_email_view(self, request, participant_id):
        # Vue pour envoyer un email à un participant spécifique via un bouton
        participant = Participant.objects.get(id=participant_id)
        message = render_to_string('email_confirmation.txt', {'participant': participant})
        send_mail(
            'Confirmation d\'inscription',
            message,
            settings.DEFAULT_FROM_EMAIL,
            [participant.email],
            fail_silently=False,
        )
        self.message_user(request, "Email de confirmation envoyé avec succès.")
        return HttpResponseRedirect("../")

    # Ajouter un bouton personnalisé dans l'affichage détaillé d'un participant
    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        participant = Participant.objects.get(pk=object_id)
        extra_context['send_email_url'] = reverse('admin:send_confirmation_email', args=[participant.id])
        return super().change_view(request, object_id, form_url, extra_context=extra_context)

    # Assurez-vous que reverse est importé
    from django.urls import reverse