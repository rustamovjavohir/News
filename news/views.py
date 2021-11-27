from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import render, redirect
from django.views.decorators.http import require_GET, require_POST

from news.forms import NewsModelForm
from news.models import News, Comment
from qalampir.util.base_utils import save_file


@require_GET
@login_required
def news_page(request):
    news_list = News.objects.filter(deleted=False)

    page = request.GET.get('page', 1)
    news = News.objects.filter(deleted=False).order_by("-id")
    pagination = Paginator(news, 2)
    news = pagination.page(page)

    content = dict({'news_list': news})
    return render(request, 'news.html', content)


@require_GET
def news_create_page(request):
    form = NewsModelForm()
    return render(request, 'create.html', {'form': form})


@require_POST
def news_create(request):
    form = NewsModelForm(request.POST)
    if form.is_valid():
        instance = form.save(commit=False)
        file = request.FILES.get('file')
        instance.image = save_file(file)
        instance.save()
        return redirect("news:news_page")
    else:
        error = form.errors['title'][0]
        messages.add_message(request, messages.ERROR, f'Error {error}', extra_tags='danger')
        return redirect('news:news_create_page')


@require_GET
def news_details_page(request, pk):
    news = News.objects.filter(pk=pk, deleted=False).first()
    context = {"news": news}
    return render(request, 'details.html', context=context)


@require_GET
def news_delete_page(request, pk):
    news = News.objects.get(pk=pk)
    context = {"news": news}
    return render(request, 'delete.html', context=context)


@require_POST
def news_delete(request, pk):
    news = News.objects.get(pk=pk)
    news.deleted = True
    news.save()
    return redirect("news:news_page")


@require_POST
@login_required
def leave_comment(request, post_id):
    news = News.objects.get(pk=post_id)
    if not news:
        raise Http404('Post Not Found')
    comment_text = request.POST.get('comment')
    comment = Comment(comment=comment_text, news=news)
    comment.created_by = request.user
    comment.save()
    return redirect('news:news_details_page', post_id)
