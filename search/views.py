from django.shortcuts import render
# from blog.models import Post

# Create your views here.
def test(request):
    return render(request, 'search/search_main.html')

def search(request):
    category = request.GET.get('choices', '')
    q = request.GET.get('q','')
    print(1)
    print(q)
    print(2)
    print(category)
    print("hello test")


    return render(request, 'search/search_main.html')
