import os
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.shortcuts import redirect
from posts.models import Post
from django.http import JsonResponse
from django.views.generic import View
from django.http import HttpResponseForbidden
import json
import markdown

from utils.utils import dispatch_decorator



@login_required
def choose_template_view(request):
    template_list=os.listdir(settings.BASE_DIR+'/templates/post_templates/create')
    return render(request, 'post_templates/choose_template.html', {'template_list': template_list})


def post_view(request, id):
    try:
        post = Post.objects.get(pk=id)
        context = {
            'post': post,
            'tags': Post.tags.cloud(steps=6),
        }
        if 'location' in post.template_name:
            context.update({'location_lat': post.media_url.split('/')[0], 'location_lng': post.media_url.split('/')[1]})
        return render(request, 'post_templates/view/{0}'.format(post.template_name), context)
    except Post.DoesNotExist:
        return redirect('feed')


@login_required
def create_post_view(request, template_name):
    if request.method == 'POST':
        request_post = json.loads(request.body.decode("utf-8"))
        post = Post.objects.create(user=request.user)
        for key, value in request_post.items():
            setattr(post, key, value)
        post.media_url = request_post['media_url'].replace("watch?v=", "v/")
        post.text_rendered = markdown.markdown(post.text)
        post.template_name = template_name
        post.save()
        return JsonResponse({'id': post.id})
    return render(request, 'post_templates/create/{0}'.format(template_name), {'tags': Post.tags.cloud(steps=6)})

@login_required
def edit_post_view(request, id):
    try:
        post = Post.objects.get(pk=id)
        if not (request.user.is_superuser or request.user == post.user):
            return redirect('/')
        return render(request, 'post_templates/edit/{0}'.format(post.template_name), {'tags': Post.tags.cloud(steps=6)})
    except Post.DoesNotExist:
        return redirect('feed')


@dispatch_decorator(login_required)
class ApiPostView(View):

    def get(self, request, id):
        post = Post.objects.get(pk=id)
        if not (request.user.is_superuser or request.user == post.user):
            return HttpResponseForbidden()
        tags = ' '.join(list(map(lambda tag: tag.name, post.tags)))
        data = {
            'text': post.text,
            'description': post.description,
            'tags': tags,
            'title': post.title,
            'media_url': post.media_url,
        }
        return JsonResponse(data)

    def patch(self, request, id):
        post = Post.objects.get(pk=id)
        if not (request.user.is_superuser or request.user == post.user):
            return HttpResponseForbidden()
        patch = json.loads(request.body.decode("utf-8"))
        for key, value in patch.items():
            setattr(post, key, value)
        post.media_url = patch['media_url'].replace("watch?v=", "v/")
        post.text_rendered = markdown.markdown(post.text)
        post.save()
        return JsonResponse({'messege': 'updated'})

    def delete(self, request, id):
        post = Post.objects.get(pk=id)
        if not (request.user.is_superuser or request.user == post.user):
            return HttpResponseForbidden()
        post.delete()
        return JsonResponse({'messege': 'deleted'})


def all_tags_view(request):
    return JsonResponse(list(map(lambda tag: tag.name, Post.tags.all())), safe=False)
