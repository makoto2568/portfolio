from django import forms 

from .models import Project, Task, Note

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('project_name', 'users', 'description', 'created_user')

class DateInput(forms.DateInput):
    inuput_type = 'date'

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['project', 'user', 'task_name', 'description', 'deadline', 'status']
        
    deadline = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))  # 日付選択用ウィジェット

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'description']

class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(label='Old Password', widget=forms.PasswordInput)
    new_password1 = forms.CharField(label='New Password', widget=forms.PasswordInput)
    new_password2 = forms.CharField(label='Confirm New Password', widget=forms.PasswordInput)

class ChangeUsernameForm(forms.Form):
    new_username = forms.CharField(label='新しいユーザーネーム', max_length=150)

class ChangeEmailForm(forms.Form):
    new_email = forms.EmailField(label='新しいメールアドレス')
 
 
