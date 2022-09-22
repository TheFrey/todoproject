from django.urls import path, re_path
from todolist import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    re_path(r'^register/$', views.register, name='register'),
    re_path(r'^delete/(?P<idx>[-\w]+)/$', views.delete_item, name='delete_item'),
    re_path(r'^modify/(?P<idx>[-\w]+)/$', views.modify_item, name='modify_item'),
    re_path(r'^(?P<idx>\d+)/(?P<date>[-\w]+)/$', views.add_sub, name='add_sub'),
    re_path(r'^login/$', views.user_login, name='login'),
    re_path(r'^logout/$',  LogoutView.as_view(template_name='logout.html'),
            name='logout'),
    path('', views.todo_list, name='todo_list'),
    re_path(r'^(?P<urgency_slug>[-\w]+)/$', views.todo_list, name='todo_list_by_urgency'),
]
