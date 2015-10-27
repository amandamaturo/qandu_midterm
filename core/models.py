from django.db import models

TITLE_CHOICES = (
(0, 'Mr.'),
(1, 'Mrs.'),
(2, 'Miss.'),
(3, 'Dr.'),
)

class Message(models.Model):
  name = models.CharField(max_length=300)
  email = models.CharField(max_length=300)
  message = models.TextField(null=True, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  title = models.IntegerField(choices=TITLE_CHOICES, default=0)

  def __unicode__(self):
    return self.email
