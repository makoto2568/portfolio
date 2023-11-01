from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Project, ProjectMember, Note, Task
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .forms import ProjectForm, TaskForm
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from .forms import NoteForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from .forms import ChangePasswordForm, ChangeUsernameForm, ChangeEmailForm

@login_required
def top(request):
    user = request.user
    projects = Project.objects.filter(users=user)
    return render(request, "home/top.html", {'projects': projects})

def project_detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    tasks = project.task_set.all()
    context = {'project': project, 'tasks': tasks}
    return render(request, "project/project_detail.html",context)

def project_new(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('top')
    
    else:
        form = ProjectForm()
    return render(request, "project/project_new.html", {'form': form})

def task_detail(request, project_id, task_id):
    project_id = int(project_id)
    task_id = int(task_id)
    task = get_object_or_404(Task, pk=task_id)
    project = get_object_or_404(Project, pk=project_id)
    tasks = Task.objects.filter(project_id=project_id)

    # 削除ボタンの追加
    if request.method == 'POST' and 'delete_task' in request.POST:
        task.delete()
        return redirect('studytracker:project_detail', project_id=project_id)
    
    context = {'project': project, 'tasks': tasks, 'task': task}
    return render(request, 'task/detail_task.html', context)

def create_task(request, project_id):
    project_id = int(project_id)
    project = get_object_or_404(Project, pk=project_id)

    if request.method == 'POST':  #HTTPリクエストのメソッドがPOSTである場合
        form = TaskForm(request.POST)  #ノート作成のフォームデータを取得
        if form.is_valid():   #バリデーションを行う
            task = form.save(commit=False)
            task.project = project
            task.save()
            return redirect('studytracker:project_detail', project_id=project_id)  #ノート一覧ページにリダイレクト
    else:  #HTTPリクエストのメソッドがPOSTでない場合
        form = TaskForm()  #空のフォームを生成

    context = {'project': project, 'form': form}
    return render(request, 'task/create_task.html', context)
    
def edit_task(request, project_id, task_id):
    project_id = int(project_id)
    task_id = int(task_id)
    project = get_object_or_404(Project, pk=project_id)
    task = get_object_or_404(Task, pk=task_id, project=project)

    if request.method == 'POST':
        # POST メソッドの場合、フォームデータを取得してバリデーションを行う
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            # フォームデータがバリデーションを通過した場合、ノートを更新（保存）して詳細ページにリダイレクトする
            form.save()
            return redirect('studytracker:task_detail', project_id=project_id, task_id=task_id)
    else:
        # POST メソッドでない場合、既存のノートデータを使用してフォームを生成する
        form = TaskForm(instance=task)

    context = {'project': project, 'task': task, 'form': form}
    return render(request, 'task/edit_task.html', context)


def setting(request):
    return render(request, "setting/setting.html")

def notes_list(request, project_id):
    project_id = int(project_id)
    project = get_object_or_404(Project, pk=project_id)
    notes = Note.objects.filter(project_id=project_id)
    context = {'project': project, 'notes': notes}
    return render(request, 'notes/notes.html', context)

def note_detail(request, project_id, note_id):
    project_id = int(project_id)
    note_id = int(note_id)
    project = get_object_or_404(Project, pk=project_id)
    note = get_object_or_404(Note, pk=note_id)
    notes = Note.objects.filter(project_id=project_id)
     
    # 削除ボタンの追加
    if request.method == 'POST' and 'delete_note' in request.POST:
        note.delete()
        return redirect('studytracker:notes_list', project_id=project_id)
    
    context = {'project': project, 'notes': notes, 'note': note}
    return render(request, 'notes/note_detail.html', context)


def create_note(request, project_id):
    project_id = int(project_id)
    project = get_object_or_404(Project, pk=project_id)

    if request.method == 'POST':  #HTTPリクエストのメソッドがPOSTである場合
        form = NoteForm(request.POST)  #ノート作成のフォームデータを取得
        if form.is_valid():   #バリデーションを行う
            note = form.save(commit=False)
            note.project = project
            note.save()
            return redirect('studytracker:notes_list', project_id=project_id)  #ノート一覧ページにリダイレクト
    else:  #HTTPリクエストのメソッドがPOSTでない場合
        form = NoteForm()  #空のフォームを生成

    context = {'project': project, 'form': form}
    return render(request, 'notes/create_note.html', context)

def edit_note(request, project_id, note_id):
    project_id = int(project_id)
    note_id = int(note_id)
    project = get_object_or_404(Project, pk=project_id)
    note = get_object_or_404(Note, pk=note_id, project=project)

    if request.method == 'POST':
        # POST メソッドの場合、フォームデータを取得してバリデーションを行う
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            # フォームデータがバリデーションを通過した場合、ノートを更新（保存）して詳細ページにリダイレクトする
            form.save()
            return redirect('studytracker:note_detail', project_id=project_id, note_id=note_id)
    else:
        # POST メソッドでない場合、既存のノートデータを使用してフォームを生成する
        form = NoteForm(instance=note)

    context = {'project': project, 'note': note, 'form': form}
    return render(request, 'notes/edit_note.html', context)

def settings(request):
    user = request.user
    projects = Project.objects.filter(users=user)
    context = {'user': user, 'projects': projects}
    return render(request, 'setting/setting.html', context)

def change_password(request):
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            user = request.user
            old_password = form.cleaned_data['old_password']
            new_password1 = form.cleaned_data['new_password1']
            new_password2 = form.cleaned_data['new_password2']
            
            if user.check_password(old_password) and new_password1 == new_password2:
                user.set_password(new_password1)
                user.save()
                update_session_auth_hash(request, user)  # セッションの認証情報を更新
                messages.success(request, 'Password changed successfully.')
                return redirect('studytracker:settings')
            else:
                messages.error(request, 'Invalid password or passwords do not match.')
    else:
        form = ChangePasswordForm()
    
    context = {'form': form}
    return render(request, 'setting/change_password.html', context)

def change_username(request):
    if request.method == 'POST':
        form = ChangeUsernameForm(request.POST)
        if form.is_valid():
            new_username = form.cleaned_data['new_username']
            user = request.user
            user.username = new_username
            user.save()
            messages.success(request, 'ユーザーネームが変更されました。')
            return redirect('studytracker:settings')
    else:
        form = ChangeUsernameForm()
    
    context = {'form': form}
    return render(request, 'setting/change_username.html', context)

def change_email(request):
    if request.method == 'POST':
        form = ChangeEmailForm(request.POST)
        if form.is_valid():
            new_email = form.cleaned_data['new_email']
            user = request.user
            user.email = new_email
            user.save()
            messages.success(request, 'メールアドレスが変更されました。')
            return redirect('studytracker:settings')
    else:
        form = ChangeEmailForm()
    
    context = {'form': form}
    return render(request, 'setting/change_email.html', context)