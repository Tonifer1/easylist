from django.db import models
from django.contrib.auth.models import User


class Notes(models.Model):
    note_id = models.AutoField(primary_key=True)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')

    def __str__(self):
        return f"Note {self.note_id} for {self.user.username}"

