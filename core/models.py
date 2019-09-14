from django.db import models


class Email(models.Model):
    email = models.EmailField(blank=False)
    submitted_from = models.URLField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        managed = True
