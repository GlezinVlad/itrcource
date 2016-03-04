"""itrcource URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from authentication.views import RegisterView, LoginView, logout_view
from feed.views import feed_view, feed_by_rating_view
from userinfo.views import profile_view, settings_view, UserInfoView, status_view
from posts.views import choose_template_view, create_post_view, post_view, edit_post_view, ApiPostView, all_tags_view
from comments.views import CommentView, delete_comment
from search.views import search_view

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login$', LoginView.as_view(), name='login'),
    url(r'^register$', RegisterView.as_view(), name='register'),
    url(r'^logout$', logout_view, name='logout'),
    url(r'^settings$', settings_view, name='settings'),
    url(r'^user_status$', status_view, name='status'),
    url(r'^userinfo$', UserInfoView.as_view(), name='userinfo'),
    url(r'^profile/(?P<username>.+)$', profile_view, name='detail'),
    url(r'^posts/create/choose_template$', choose_template_view, name='choose_template'),
    url(r'^posts/create/(?P<template_name>.+)$', create_post_view, name='create_post'),
    url(r'^posts/edit/(?P<id>.+)$', edit_post_view, name='edit_post'),
    url(r'^posts/(?P<id>.+)$', post_view, name='post'),
    url(r'tags$', all_tags_view, name='all_tags'),
    url(r'^api/posts/comments/(?P<post_id>.+)$', CommentView.as_view(), name='comments_by_post'),
    url(r'^api/comments/(?P<id>.+)$', delete_comment, name='delete_comment'),
    url(r'^api/posts/(?P<id>.+)$', ApiPostView.as_view(), name='post_api'),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^ratings/', include('star_ratings.urls', namespace='ratings', app_name='ratings')),
    url(r'^search$', search_view, name='search'),
    url(r'^by_rating$', feed_by_rating_view, name='feed_by_rating'),
    url(r'^$', feed_view, name='feed'),
]
