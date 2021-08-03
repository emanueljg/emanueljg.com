from django.urls import path
from django.views.generic.base import RedirectView

from . import views

urlpatterns = [
    path('', views.start, name='base-start'),
    path('blog/', RedirectView.as_view(url='page/1/'), name='base-blog'),
    path('blog/page/<int:n>/', views.blog_page, name='base-blog_page'),
    path('blog/post/<int:n>/', views.blog_post, name='base-blog_post')
]