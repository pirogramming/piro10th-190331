from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
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

# 수정, 삭제