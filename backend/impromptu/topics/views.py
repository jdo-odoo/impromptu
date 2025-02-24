from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from topics.models import Topic,Category

def TopicList(request):
    topics = Topic.objects.all().order_by('-publish')
    categories = Category.objects.filter(parent__isnull=True)
    context = {
        'topics':topics,
        'categories':categories,
    }
    template = 'topics/topics_list.html'
    return render(request, template ,context)


def Topics_by_category(request,category_slug):
    topics = Topic.objects.all()
    categories = Category.objects.filter(parent__isnull=True)
    slug = category_slug
    if slug:
        category_s = get_object_or_404(Category,slug = slug)    
        topics = topics.filter(category = category_s)
    paginator = Paginator(topics, 25)  # Show 25 topics per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        'topics':topics,
        'categories':categories,
        'category':category_s,
        'page_obj':page_obj,
    }
    template = 'topics/topics_by_category_list.html'
    return render(request,template,context)
