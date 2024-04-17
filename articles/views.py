from django.shortcuts import render
from articles.models import Article


def article_all(request):
    maqolalar = Article.objects.all().order_by('-id')
    context = {
        'maqolalar': maqolalar
    }
    return render(request, 'maqola.html', context=context)
