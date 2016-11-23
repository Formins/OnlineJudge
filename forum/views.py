# -*- coding: utf-8 -*-
import markdown2 as markdown2
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import FormView
# Create your views here.
from forum.form import CreateArticleForm, CommentForm
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
    author = article.author
    return render(request, 'oj/forum/article_page.html', {
        'article': article,
        'author': author,
        'content': content,
        'comments': comments
    })


def create_article(request):
    user = request.user
    if request.method == 'POST':
        form = CreateArticleForm(request.POST)
        if form.is_valid():
            # article.author_id = user.id
            # article.author = user.username
            new_article = form.save()
            return HttpResponseRedirect('/forum/article/' + str(new_article.pk))
    else:
        form = CreateArticleForm()

    context = {
        'user': user,
        'form': form,

    }
    return render(request, "oj/forum/create_article.html", context)


def post_comment(request):
    article_id = request.POST.get("article_id", "")
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/forum/article/' + str(article_id))
    else:
        form = CommentForm()

    context = {
        'commentform': form,
    }
    return render("oj/forum", context)
