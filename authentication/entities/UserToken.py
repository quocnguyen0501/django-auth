from django.db import models
from django.utils import timezone

from authentication.entities.User import User


class UserToken(models.Model):
  id = models.AutoField(primary_key=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  refresh_token = models.TextField(db_column='refresh_token')
  access_token = models.TextField(db_column='access_token')
  created_at = models.DateTimeField(db_column='created_at', default=timezone.now)
  updated_at = models.DateTimeField(db_column='updated_at', default=timezone.now)

  class Meta:
    db_table = 'user_token'

  def __str__(self):
    return f"UserToken {self.id}"
