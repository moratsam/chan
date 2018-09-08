from django.contrib.auth import authenticate, get_user_model, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Thread, Comment
from .forms import ThreadForm, CommentForm, LoginForm

@login_required(login_url='/login/')
def thread_list(request):
    queryset = Thread.objects.order_by('-timestamp')
    context={
        "obj_list": queryset,
    }
    return render(request, "thread/list.html", context)

@login_required(login_url='/login/')
def thread_details(request, id=None):
    instance=get_object_or_404(Thread, id=id)
    comments = Comment.objects.filter(thread_id=instance.id)
    context={
        "obj": instance,
        "comments": comments,
    }
    return render(request, "thread/detail.html", context)

@login_required(login_url='/login/')
def thread_create(request):
    form=ThreadForm(request.POST or None, request.FILES or None)
    if form.is_valid():
            form.save()
            return HttpResponseRedirect("/catalog/")
    context={
        "form": form,
    }
    return render(request, "thread/form.html", context)

@login_required(login_url='/login/')
def thread_comment(request, id=None):
    instance=get_object_or_404(Thread, id=id)
    initial_data={
        "thread_id": instance.id,
        "user": request.user,
    }
    form=CommentForm(request.POST or None, request.FILES or None, initial=initial_data)
    if form.is_valid():
        ins=form.save(commit=False)
        ins.user=request.user
        ins.thread_id=instance.id
        ins.save()
        return HttpResponseRedirect("/thread/"+str(instance.id)+"/")
    context={
        "form": form,
    }
    return render(request, "thread/comment_form.html", context)

@login_required(login_url='/login/')
def reply(request, id=None, id2=None):
    instance=get_object_or_404(Thread, id=id)
    initial_data={
        "user": request.user,
        "thread_id": instance.id,
        "parent_id": id2,
    }
    form=CommentForm(request.POST or None, request.FILES or None, initial=initial_data)
    if form.is_valid():
        ins=form.save(commit=False)
        ins.user=request.user
        ins.thread_id=instance.id
        ins.parent_id=id2
        ins.save()
        return HttpResponseRedirect("/thread/"+str(instance.id)+"/")
    context={
        "form": form,
    }
    return render(request, "thread/comment_form.html", context)

def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username=form.cleaned_data.get("username")
        password=form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)
        return HttpResponseRedirect("/catalog/")
    return render(request, "thread/login_form.html", {"form": form})
