from django.shortcuts import render
from .forms import blogform,signupform,commentform
from django.shortcuts import redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import Blogmodel,commentmodel ,Profile
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.core.mail import send_mail
from django.conf import settings 
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger


def home(request):
   return render(request,'blogapp/home.html')

def authorview(request,pk):
    user=User.objects.get(id=pk)
    a=Blogmodel.objects.filter(author_id=pk).order_by('-published_date')
    p=str(request.user)
    q=str(user.username)
    context={'user':user,'a':a ,'p':p,"q":q,}
    return render(request,'blogapp/authorview.html',context)
   
def blogview(request):
    form=blogform()
    new_form=None
    if request.method=='POST':
        form=blogform(request.POST)
        if form.is_valid():
           new_form=form.save(commit=False)
           new_form.author=request.user
           new_form.save()
           return redirect('/blogapp/blog/')
        else:
           return  redirect('home')
    else:
        form=blogform()
    context={'form':form}
    return render(request,'blogapp/blog.html',context)

def blogretrieve(request):
   blogmodel=Blogmodel.objects.all().order_by('-published_date')
   page=request.GET.get('page')
   paginator=Paginator(blogmodel, 3)
   #blogmodel=paginator.page(page)
   try:
      blogmodel=paginator.page(page)
   except PageNotAnInteger:
      blogmodel=paginator.page(1)
   except EmptyPage:
    # If page is out of range deliver last page of results
      blogmodel= paginator.page(paginator.num_pages)

   context={'blogmodel':blogmodel,'paginator':paginator}
   return render(request,'blogapp/blogretrieve.html',context)

def blog(request,pk):
    #blogmodel=Blogmodel.objects.filter(id=pk)
 
   blog = get_object_or_404(Blogmodel, pk=pk)
    #comments=blogmodel.comments.all()
    #context={'blogmodel':blogmodel,'comments':comments}
   comments = blog.comments.all()
   form=commentform()
   new_comment=None
   if request.method=='POST':
      form=commentform(request.POST)
      if form.is_valid():
         new_comment=form.save(commit=False)
         new_comment.blogmodel=blog
         new_comment.user=request.user
         new_comment.save()
         
         #return redirect('blogapp/blogdata/')
         return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
   else:
      form=commentform()
  # context = {'blog': blog, 'comments':comments,'form':form,'new_comment':new_comment}
   return render(request,'blogapp/blogpk.html', {'blog': blog, 'comments':comments,'form':form,'new_comment':new_comment})

def signupview(request):
   form=signupform()
   if request.method=='POST':
      form=signupform(request.POST)
      #email=request.POST.get('email')                   #we can also use this inplace of receiver email [email]
      #email=form.cleaned_data['email']
      #if User.objects.filter(username=username).first():
      #   message.succes(request,'username is taken ')
      if form.is_valid():
        form.save()
        #sending welcome mail
        subject='welcome to blog '
        message='its our pleasure to have you '               #form.cleaned_data will bu used after form.is_valid 
        send_mail(subject, message, settings.EMAIL_HOST_USER, [form.cleaned_data['email']],fail_silently=False,)
        #login after signup
        username = form.cleaned_data['username']
        password = form.cleaned_data['password1']
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('/blogapp/')
   else:
      form=signupform()  
   context={'form':form}
   return render(request,'blogapp/signupform.html',context)

def loginview(request):
   if request.method=='POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)
      return redirect(f'/blogapp/author/{user.pk}/')
        
    else:
        return redirect('/blogapp/signup/')
    #context={'username':username,'password':password}
   return render(request,'blogapp/loginview.html')    
def logoutview(request):
   logout(request)
   return render(request,'blogapp/logoutview.html')

def profile(request,pk):
   user=User.objects.get(id=pk)
   profile=Profile(user=user)
   profile.save()
   context={'profile':profile,'user':user}
   return render(request,'blogapp/profile.html',context)



def password_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
    else:
       form=PasswordChangeForm(user=request.user)
    return render(request,'blogapp/passwordchange.html',{'form':form})

