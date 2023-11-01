from django.db import models
from django.contrib.auth.models import User
import secrets

class Project(models.Model):
    project_id = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=100, null=True)
    users = models.ManyToManyField(User)
    # description of oneself
    description = models.TextField()
    # will change this to a choice field someday
    created_user = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.project_name

class ProjectMember(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role_choices = [
        ('admin', '管理者'),
        ('member', 'メンバー'),
        ('limited_member', '制限メンバー'),
        ('folder_guest', 'フォルダゲスト'),
    ]
    role = models.CharField(max_length=50, choices=role_choices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} ({self.role})"

class Note(models.Model):
    note_id = models.AutoField(primary_key=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class Task(models.Model):
    STATUS_CHOICES = (
        ('Not Started', '実行前'),
        ('In Progress', '実行中'),
        ('Under Review', 'レビュー中'),
        ('Completed', '完了'),
    )
    task_id = models.AutoField(primary_key=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=200)
    description = models.TextField()
    deadline = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Not Started')
    completed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.task_name
    
