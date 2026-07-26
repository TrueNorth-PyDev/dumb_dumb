from django.db import models

class WaitlistEntry(models.Model):
    name = models.CharField(max_length=255)
    business_name = models.CharField(max_length=255)
    contact = models.CharField(max_length=255, verbose_name="WhatsApp or Email")
    platform = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.business_name} - {self.name}"
