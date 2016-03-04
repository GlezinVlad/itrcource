from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from posts.models import Post
from comments.models import Comment
from django.http import JsonResponse
from django.views.generic import View
from django.http import HttpResponseForbidden
from django.views.decorators.http import require_http_methods
import json




class CommentView(View):

    def get(self, request, post_id):
        post = Post.objects.get(pk=post_id)
        comments = list(map(lambda comment:  {
            'id': comment.id,
            'username': comment.user.username,
            'user_avatar_url': comment.user.userinfo.avatar_url,
            'fullname': comment.user.userinfo.fullname(),
            'time_published': comment.time_published,
            'text': comment.text,
        }, post.comment_set.all().order_by('time_published')))
        return JsonResponse(comments, safe=False)

    @method_decorator(login_required)
    def post(self, request, post_id):
        request_post = json.loads(request.body.decode("utf-8"))
        comment = Comment.objects.create(user=request.user, post=Post.objects.get(pk=post_id), text=request_post['text'])
        comment.save()
        return JsonResponse({
            'id': comment.id,
            'username': comment.user.username,
            'user_avatar_url': comment.user.userinfo.avatar_url,
            'fullname': comment.user.userinfo.fullname(),
            'time_published': comment.time_published,
            'text': comment.text,
        })

@login_required
def delete_comment(request, id):
    comment = Comment.objects.get(pk=id)
    if not (request.user.is_superuser or request.user == comment.user):
        return HttpResponseForbidden()
    comment.delete()
    return JsonResponse({'messege': 'deleted'})

