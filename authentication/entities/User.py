from django.db import models
from django.core.validators import EmailValidator
from django.utils import timezone


class User(models.Model):
  id = models.AutoField(db_column='id', primary_key=True)
  email = models.EmailField(
    db_column='email',
    validators=[EmailValidator],
    unique=True
  )
  password = models.CharField(db_column='password', max_length=255, null=True)
  phone = models.CharField(db_column='phone', max_length=30, null=True)
  name = models.CharField(db_column='name', max_length=255, null=False)
  status = models.IntegerField(db_column='status', default=0)
  created_at = models.DateTimeField(db_column='created_at', default=timezone.now)
  updated_at = models.DateTimeField(db_column='updated_at', default=timezone.now)

  class Meta:
    db_table = 'user'

  def __str__(self):
    return str(self.id) + "_" + str(self.email)
