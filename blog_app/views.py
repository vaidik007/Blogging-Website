from django.shortcuts import render
from .models import blog_post
# Create your views here.

class postlist(generic.ListView):
    queryset = blog_post.objects.filter(status = 1).order_by('-created_on')
    template_name = 'index.html'



#class postdetail(generic.DetailView):
        #model = 
