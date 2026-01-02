from django.db import models

class Inquiry(models.Model):
    name = models.CharField(max_length=255, verbose_name="Full Name")
    email = models.EmailField(verbose_name="Email Address")
    message = models.TextField(verbose_name="Project Brief")
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Project Inquiry"
        verbose_name_plural = "Project Inquiries"
        ordering = ['-created_at']

    def __str__(self):
        return f"Inquiry from {self.name} - {self.email}"