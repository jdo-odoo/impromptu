from django.shortcuts import render

def TopicList(request):
    topics = Topic.objects.all()
    products = products.order_by('-publish')
    categories = Category.objects.filter(parent__isnull=True)
    context = {
        'products':products,
        'categories':categories,
    }
    template = 'products/product_list.html'
    return render(request, template ,context)


def Topics_by_category(request,category_slug):
    topics = Topic.objects.all()
    categories = Category.objects.filter(parent__isnull=True)
    slug = category_slug
    if slug:
        category_s = get_object_or_404(Category,slug = slug)    
        topics = topics.filter(category = category_s)
    context = {
        'topics':topics,
        'categories':categories,
        'category':category_s,
        'page_obj':page_obj,
    }
    template = 'topics/topics_by_category_list.html'
    return render(request,template,context)
