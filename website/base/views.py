from django.db.models.aggregates import Count
from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import BadRequest
from .models import Post

PAGE_LIMIT = 10

# 1
# 0 to 9
# 2
# 11 to 20
# 3
# 21

def _get_last_page_n():
    return -(-Post.objects.count() // PAGE_LIMIT)

def _get_last_post_n():
    return Post.objects.last().pk

def extend_with_pagination(d, n, last_element_n_func):
    return {
        'first'      :  '../1/',
        'previous'   : f'../{n-1}/' if n > 1 else None,
        'current'               : str(n),
        'next'       : f'../{n+1}/' if n < last_element_n_func() else None,
        'last'       : f'../{last_element_n_func()}/',
        **d
    }

def start(request):
    return render(request, 'base/start.html')

def blog_page(request, n):
    context = {
        'posts'           : Post.objects.all()[(n-1)*PAGE_LIMIT:n*PAGE_LIMIT]
    }
    extended_context = extend_with_pagination(context, n, _get_last_page_n)
    return render(request, 'base/blog_page.html', extended_context)

def blog_post(request, n):
    context = {
        'post': Post.objects.get(pk=n)
    }
    extended_context = extend_with_pagination(context, n, _get_last_post_n)
    return render(request, 'base/blog_post.html', context)


