from django.shortcuts import render_to_response, render
from endless_pagination.decorators import page_template
from django.template import RequestContext
from posts.models import Post
from tagging.models import Tag, TaggedItem


@page_template('post_templates/post_mini.html')
def search_view(request, template='search.html', extra_context=None):
    if request.GET:
        extra_context.update({'q': request.GET['q']})
        if Tag.objects.filter(name=request.GET['q']).exists():
            extra_context.update({
                'posts': TaggedItem.objects.get_by_model(Post, Tag.objects.filter(name=request.GET['q'])).order_by('-ratings__average')
            })
    context = {
        'posts': Post.objects.none(),
        'tags': Post.tags.cloud(steps=6),
    }
    if extra_context is not None:
        context.update(extra_context)
    return render_to_response(template, context, context_instance=RequestContext(request))
