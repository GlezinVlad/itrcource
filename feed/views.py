from django.shortcuts import render_to_response
from endless_pagination.decorators import page_template
from django.template import RequestContext
from posts.models import Post


@page_template('post_templates/post_mini.html')
def feed_view(request, template='feed.html', extra_context=None):
    context = {
        'posts': Post.objects.all().order_by('-date_published'),
        'tags': Post.tags.cloud(steps=6),
    }
    if extra_context is not None:
        context.update(extra_context)
    return render_to_response(template, context, context_instance=RequestContext(request))


@page_template('post_templates/post_mini.html')
def feed_by_rating_view(request, template='feed_by_rating.html', extra_context=None):
    context = {
        'posts': Post.objects.order_by('-ratings__average'),
        'tags': Post.tags.cloud(steps=6),
    }
    if extra_context is not None:
        context.update(extra_context)
    return render_to_response(template, context, context_instance=RequestContext(request))
