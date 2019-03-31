from django.shortcuts import render, get_object_or_404, redirect
# from blog.models import Post
from django.contrib.auth.models import User

# Create your views here.
def test(request):
    return render(request, 'search/search_main.html')

def search(request):
    category = request.GET.get('choices', '')
    print(category)

    # if category == 'Title':
    #     qs = Post.objects.all()
    #     q = request.GET.get('q', '')
    #     if q:
    #         result = []
    #         qs = qs.filter(title__icontains=q)
    #         for qp in qs:
    #             result.append(get_object_or_404(Post, pk=qp.id))
    #         return render(request, 'search/search_result.html', {
    #             'result': result,
    #         })
    #
    # elif category == 'Content':
    #     qs = Post.objects.all()
    #     q = request.GET.get('q', '')
    #     if q:
    #         result = []
    #         qs = qs.filter(content__icontains=q)
    #         for qp in qs:
    #             result.append(get_object_or_404(Post, pk=qp.id))
    #         return render(request, 'search/search_result.html', {
    #             'result': result,
    #         })

    if category == 'User':
        qs = User.objects.all()
        q = request.GET.get('q', '')
        if q:
            result = []
            qs = qs.filter(username__icontains=q)
            for qp in qs:
                result.append(get_object_or_404(User, pk=qp.id))
            return render(request, 'search/search_result.html', {
                'result': result,
                'q': q,
            })


    else:
        return redirect('search:test')
