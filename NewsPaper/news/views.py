from datetime import datetime
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *


class PostList(ListView):
    model = Post
    ordering = '-rating'
    template_name = 'news.html'
    context_object_name = 'news'

    #def get_context_data(self, **kwargs):
     #   context = super().get_context_data(**kwargs)
      #  context['time_now'] = datetime.utcnow()
        #context['next_sale'] = "Распродажа в среду!"
       # return context


class PostDetail(DetailView):
    model = Post
    ordering = 'name'
    template_name = 'news_id.html'
    context_object_name = 'post'



