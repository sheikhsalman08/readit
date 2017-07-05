"""forum URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib.auth.decorators import login_required
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.contrib import admin

from student_post.views import (list_posts, Students_list, Post_details, insert_post, Insert_post_ClassBassed, CreateStudent)

urlpatterns = [
    #auth
    url(r'^logout/$', auth_views.logout,{'next_page':'home'}, name='logout'),
    url(r'^login/$', auth_views.login,{'template_name':'login.html'}, name='login'),

    #admin
    url(r'^admin/', admin.site.urls),
    url(r'^$', list_posts, name='home'),
    url(r'^insert_post_classbassed/$', Insert_post_ClassBassed.as_view(), name='Insert_post_ClassBassed'),
    url(r'^students/$', Students_list.as_view(), name='students'),
    url(r'^students/add$', login_required(CreateStudent.as_view()), name='createStudentCreateView'),
    url(r'^post/(?P<pk>[-\w]+)/$', Post_details.as_view(), name='post_details'),
    url(r'^insert_post/(?P<pk>[-\w]+)/$', insert_post, name='insert_post'),
]
