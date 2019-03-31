from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect

from bulletin.forms import PostForm
from .models import Document
# Create your views here.

def documentList(request):
    docs = Document.objects.all()
    pages = Paginator(docs, 10)
    page = request.GET.get('page')
    list = pages.get_page(page)

    return render(request, 'bulletin/docList.html', {
        "list": list
    })

def detailView(request, id):
    doc = get_object_or_404(Document, pk=id)
    return render(request, 'bulletin/detail.html', {
        "doc": doc
    })

@login_required
def newPost(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('document', id=post.id)

    else:
        form = PostForm()
        return render(request, 'newPost.html', {
            'form':form
        })

# 수정, 삭제


@login_required
def deleteDoc(request, id):
    pass


@login_required
def modifyDoc(request, id):
    pass
