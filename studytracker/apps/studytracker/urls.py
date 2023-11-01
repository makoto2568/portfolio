from django.urls import path
from . import views
from apps.studytracker import views


app_name = 'studytracker'

urlpatterns = [
    path('<int:project_id>', views.project_detail, name='project_detail'),
    path('project/', views.project_new, name='project_new'),
    path('<int:project_id>/notes_list/', views.notes_list, name='notes_list'),
    path('<int:project_id>/notes_list/<int:note_id>/', views.note_detail, name='note_detail'),
    #ノート新規作成するページ
    path('<int:project_id>/note_list/create_note/', views.create_note, name='create_note'),
    #既存のノートを編集するページ
    path('<int:project_id>/note_list/<int:note_id>/edit_note/', views.edit_note, name='edit_note'),
    path('<int:project_id>/<int:task_id>/', views.task_detail, name='task_detail'),
    path('<int:project_id>/create_task/', views.create_task, name='create_task'),
    path('<int:project_id>/<int:task_id>/edit_task/',views.edit_task, name='edit_task'),
    path('settings/', views.settings, name='settings'),
    path('settings/change_password/', views.change_password, name='change_password'),
    path('settings/change_username/', views.change_username, name='change_username'),#ユーザーネーム変更
    path('settings/change_email/', views.change_email, name='change_email'),#メールアドレス変更

]
