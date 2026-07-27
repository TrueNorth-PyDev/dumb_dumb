from django.db import models

class WaitlistEntry(models.Model):
    name = models.CharField(max_length=255)
    business_name = models.CharField(max_length=255)
    contact = models.CharField(max_length=255, verbose_name="WhatsApp or Email")
    product_category = models.CharField(max_length=255, blank=True, null=True)
    business_duration = models.CharField(max_length=255, blank=True, null=True)
    order_volume = models.CharField(max_length=255, blank=True, null=True)
    sales_channels = models.JSONField(default=list, blank=True, null=True)
    current_tools = models.CharField(max_length=255, blank=True, null=True)
    time_drains = models.JSONField(default=list, blank=True, null=True)
    frustrations = models.JSONField(default=list, blank=True, null=True)
    lost_money = models.CharField(max_length=10, blank=True, null=True)
    lost_money_details = models.TextField(blank=True, null=True)
    desired_automation = models.CharField(max_length=255, blank=True, null=True)
    worst_task = models.TextField(blank=True, null=True)
    two_hours_saved = models.TextField(blank=True, null=True)
    interest_level = models.CharField(max_length=255, blank=True, null=True)
    biggest_slowdown = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.business_name} - {self.name}"
