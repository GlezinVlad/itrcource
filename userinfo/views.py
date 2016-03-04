from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from userinfo.models import UserInfo
from posts.models import Post
from django.http import JsonResponse
from django.shortcuts import redirect
from django.contrib.auth.models import User
from endless_pagination.decorators import page_template
from django.template import RequestContext
import json

from utils.utils import dispatch_decorator


@login_required
def settings_view(request):
    return render(request, 'user_settings.html')


@page_template('post_templates/post_mini.html')
def profile_view(request, username, template='profile.html', extra_context=None):
    profile_user = User.objects.filter(username=username)
    if profile_user.exists():
        context = {
            'profile_info': profile_user[0].userinfo,
            'posts': Post.objects.filter(user=profile_user[0]).order_by('-date_published'),
            'tags': Post.tags.cloud(steps=5),
        }
        if extra_context is not None:
            context.update(extra_context)
    return render_to_response(template, context, context_instance=RequestContext(request))


@dispatch_decorator(login_required)
class UserInfoView(View):

    def get(self, request):
        return JsonResponse(dict(request.user.userinfo.attrs()))

    def put(self, request):
        info = UserInfo.objects.get(pk=request.user.id)
        put = json.loads(request.body.decode("utf-8"))
        put['date_of_birth'] = None if not put['date_of_birth'] else put['date_of_birth'][:10]
        for key, value in put.items():
            setattr(info, key, value)
        info.save()
        return render(request, 'user_settings.html', {'message': 'Done'})


@login_required
def status_view(request):
    if request.user.is_anonymous():
        return JsonResponse({'username': '', 'is_superuser': False})
    else:
        return JsonResponse({'username': request.user.username, 'is_superuser': request.user.is_superuser})
