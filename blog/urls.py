"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myblog.views import IndexView, ArichiveView, TagDetailView, BlogDetailView,TagView,login,BlogDetailView_private
from django.conf.urls import url
from myblog.views import AddCommentView
from myblog.feeds import BlogRssFeed
from myblog.views import CategoryDetaiView
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name='index'),  #首页的url
    url(r'^index/$', IndexView.as_view(), name='index'),  #首页的url
    url(r'^archive/$', ArichiveView.as_view(), name='archive'),
    url(r'^tags/(?P<tag_name>\w+)$', TagDetailView.as_view(), name='tag_name'),
    url(r'^tags/$', TagView.as_view(), name='tags'),
    url(r'^blog/(?P<blog_id>\d+)$', BlogDetailView.as_view(), name='blog_id'),
    url(r'^blog/(?P<private_test>\d+)$', BlogDetailView_private.as_view(), name='private_test'),
    url(r'^add_comment/$', AddCommentView.as_view(), name='add_comment'),
    url(r'^rss/$', BlogRssFeed(), name='rss'),
    url(r'^category/(?P<category_name>\w+)/$', CategoryDetaiView.as_view(), name='category_name'),
    url(r'login/', login, name='login'),

]
