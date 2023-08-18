from django.shortcuts import render
from django.core.paginator import Paginator
from blog.models import Post

PER_PAGE = 9
# Create your views here.
def index(request):

    posts = Post.objects.get_published()
    paginator = Paginator(posts, PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog/index.html', { 'page_obj' : page_obj,})


def page(request):
    

    return render(request, 'blog/page.html')

def post(request,slug):
    post = Post.objects.get_published().filter(slug=slug).first()
    

    return render(request, 'blog/post.html', {'post':post,})