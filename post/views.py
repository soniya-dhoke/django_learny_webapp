from django.shortcuts import render,redirect,get_object_or_404
from .forms import PostCreateForm
from .models import Post
from django.http import HttpResponse
import json 
from taggit.models import Tag
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def createPost(request):
    form = PostCreateForm()
    if request.method == 'POST':
        form = PostCreateForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author = request.user
            obj.save()
            form.save_m2m()
            return redirect('most_recent_post')
        else :
            print(form.errors)
    context = {'form':form }
    return render(request,'post/createPost.html',context)

def getPaginatedPosts(all_posts,page):
    paginator = Paginator(all_posts,3)
    posts = paginator.get_page(page)
    nums = "a" * posts.paginator.num_pages
    most_common_tags = Post.tags.most_common()[:10]
    context={"posts":posts,"nums":nums,"most_common_tags":most_common_tags}
    return context

@login_required(login_url='login')
def mostLikedPost(request):
    all_posts = Post.objects.order_by('-likes_count')
    page = request.GET.get('page')
    return render(request,'post/displayPost.html',getPaginatedPosts(all_posts,page))

@login_required(login_url='login')
def mostRecentPost(request):
    all_posts = Post.objects.order_by('-date_posted')
    page = request.GET.get('page')
    return render(request,'post/displayPost.html',getPaginatedPosts(all_posts,page))
    
@login_required(login_url='login')
def likePost(request):
    if request.method =="POST":
        id = int(request.POST.get('post_id'))
        post = get_object_or_404(Post, id=id)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
            liked=False
        else:
            post.likes.add(request.user)
            liked=True
        post.likes_count= post.likes.count()
        post.save()
        context={"likes_count":post.likes_count,"liked":liked,"post_id":id}
        return HttpResponse(json.dumps(context), content_type='application/json')

@login_required(login_url='login')
def search(request,tag_slug=None):
    if request.method == "POST":
        tag_slug = request.POST.get('search') 
    tags = Tag.objects.filter(slug=tag_slug).values_list('name', flat=True)
    all_posts = Post.objects.filter(tags__name__in=tags).order_by('-likes_count') 
    if all_posts.exists():
        page = request.GET.get('page')
        return render(request,'post/displayPost.html',getPaginatedPosts(all_posts,page))
    else:
        search_message= "No post for the tag!!"
        most_common_tags = Post.tags.most_common()[:10] 
        context={"search_message":search_message,"most_common_tags":most_common_tags}
        return render(request,'post/displayPost.html',context)




