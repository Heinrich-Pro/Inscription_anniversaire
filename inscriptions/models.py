from django.db import models

class Participant(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    message = models.TextField(blank=True, null=True)
    date_inscription = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom
