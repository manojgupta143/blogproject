from django.shortcuts import render,get_object_or_404
from.models import Post
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.contrib.auth.decorators import login_required
# Create your views here.
from taggit.models import Tag
def post_view(request,tag_slug=None):
    post_list=Post.objects.all()
    tag=None
    if tag_slug:
        tag=get_object_or_404(Tag,slug=tag_slug)
        post_list=post_list.filter(tags__in=[tag])
    paginator=Paginator(post_list,3)
    page_number=request.GET.get('page')
    try:
        post_list=paginator.page(page_number)
    except PageNotAnInteger:
        post_list=paginator.page(1)
    except EmptyPage:
        post_list=paginator.page(paginator.num_pages)
    return render(request,'blog/home.html',{'post_list':post_list,'tag':tag})
from Blog.models import Comment 
from Blog.forms import CommentForm 
@login_required
def post_detail_view(request,year,month,day,post): 
    post=get_object_or_404(Post,slug=post, 
    status='published', 
    publish__year=year, 
    publish__month=month, 
    publish__day=day) 
    comments=post.comments.filter(active=True) 
    csubmit=False 
    if request.method=='POST': 
        form=CommentForm(data=request.POST) 
        if form.is_valid(): 
            new_comment=form.save(commit=False) 
            new_comment.post=post 
            new_comment.save() 
            csubmit=True 
    else:
        form=CommentForm() 
    return render(request,'blog/detail.html',{'post':post,'comments':comments,'csubmit':csubmit,'form':form}) 
#from django.core.mail import send_mail
from django.core.mail import send_mail
from Blog.forms import EmailsendForm
@login_required
def email_send_view(request,id):
    post=get_object_or_404(Post,id=id,status='published') 
    sent=False
    if request.method=='POST':
        form=EmailsendForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            post_url=request.build_absolute_uri(post.get_absolute_url()) 
            subject='{}({}) recommends you to read "{}"'.format(cd['name'],cd['email'],post.title) 
            message="Read Post At: \n {}\n\n{}\' Comments\n{}".format(post_url,cd['name'],cd['comment'])
            send_mail(subject,message,'rdxxyz.1212@gmail.com',[cd['to']],fail_silently=False,)
            sent=True
    else:
        form=EmailsendForm()
    return render(request,'blog/emailshare.html',{'form':form,'post':post,'sent':sent})
from Blog.forms import SignupForm
from django.http import HttpResponseRedirect
def signup_form(request): 
    form=SignupForm() 
    if request.method=='POST': 
       form=SignupForm(request.POST) 
       if form.is_valid():
         user=form.save() 
         user.set_password(user.password) 
         user.save() 
         return HttpResponseRedirect('/accounts/login/') 
    else:
        return render(request,'blog/signup.html',{'form':form})
def logout_view(request): 
    return render(request,'blog/logout.html') 