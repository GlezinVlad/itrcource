from django.http import HttpResponseRedirect
from django.conf import settings
from django.utils.decorators import method_decorator


def anonymous_required(view_function, redirect_url=settings.LOGIN_REDIRECT_URL):
    return AnonymousRequired(view_function, redirect_url)


class AnonymousRequired(object):
    def __init__(self, view_function, redirect_url):
        self.view_function = view_function
        self.redirect_url = redirect_url

    def __call__(self, request, *args, **kwargs):
        if request.user.is_anonymous():
            return self.view_function(request, *args, **kwargs)
        return HttpResponseRedirect(self.redirect_url)


def dispatch_decorator(decorator):
    def inner(cls):
        orig_dispatch = cls.dispatch

        @method_decorator(decorator)
        def new_dispatch(self, request, *args, **kwargs):
            return orig_dispatch(self, request, *args, **kwargs)
        cls.dispatch = new_dispatch
        return cls
    return inner
