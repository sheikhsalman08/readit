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
from django.conf.urls import url
from django.contrib import admin

from student_post.views import list_posts, Students_list, Post_details

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', list_posts, name='posts'),
    url(r'^students/$', Students_list.as_view(), name='students'),
    url(r'^post/(?P<pk>[-\w]+)/$', Post_details.as_view(), name='post_details'),
]
