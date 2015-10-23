from django.db import models

class Message(models.Model):
  Name = models.Charfield(max_length=300)
  Email = models.CharField(max_length=300)
  Message = models.TextField(null=True, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
