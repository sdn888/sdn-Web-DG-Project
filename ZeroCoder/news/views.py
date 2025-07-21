from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import News_postForm
from .models import News_post  # <-- добавь!

@login_required
def create_news(request):
    error = ''
    if request.method == 'POST':
        form = News_postForm(request.POST)
        if form.is_valid():
            news_post = form.save(commit=False)
            news_post.author = request.user
            news_post.save()
            return redirect('news_home')
        else:
            error = form.errors.as_ul()
    else:
        form = News_postForm()

    context = {'form': form, 'error': error}
    return render(request, 'news/add_new_post.html', context)

def home(request):
    posts = News_post.objects.all()  # <-- исправлено
    return render(request, 'news/news.html', {'posts': posts})
