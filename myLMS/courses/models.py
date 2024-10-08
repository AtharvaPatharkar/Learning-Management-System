from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    video = models.FileField(upload_to='videos/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Progress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    completion_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.user} - {self.course} - {self.completed}'

from djongo import models

class UserActivityLog(models.Model):
    user = models.CharField(max_length=100)
    activity = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "user_activity_logs"
