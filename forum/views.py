# -*- coding: utf-8 -*-
import markdown2 as markdown2
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from forum.form import CreateArticleForm
from forum.models import Article


def article_list_page(request):
    article_list = Article.objects.query_by_time()
    context = {'article_list': article_list}
    return render(request, "oj/forum/article_list.html", context)


def article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    content = markdown2.markdown(article.content,
                                 extras=["code-friendly", "fenced-code-blocks", "header-ids", "toc", "metadata"])
    comments = article.comment_set.all

    return render(request, 'oj/forum/article_page.html', {
        'article': article,
        'content': content,
        'comments': comments
    })


def create_article(request):
    user = request.user
    if request.method == 'POST':
        form = CreateArticleForm(request.POST)
        if form.is_valid():
            article.author_id = user.id
            new_article = form.save()
            return HttpResponseRedirect('/forum/article/' + str(new_article.pk))
    else:
        form = CreateArticleForm()

    context = {
        'user': user,
        'form': form,

    }
    return render(request, "oj/forum/create_article.html", context)
