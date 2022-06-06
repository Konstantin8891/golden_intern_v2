from django.contrib.auth.decorators import login_required
from django.http import FileResponse
from django.shortcuts import redirect, render

from .forms import InMemoriesForm
from .models import InMemories


def index(request):
    template = 'memo/index.html'
    return render(request, template)


@login_required
def profile(request):
    form = InMemoriesForm(request.POST or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.user = request.user
        post.save()
        return redirect('memo:profile')
    posts = InMemories.objects.filter(user=request.user)
    is_nothing = False
    if not posts.exists():
        is_nothing = True
    context = {'form': form, 'posts': posts, 'is_nothing': is_nothing}
    return render(request, 'memo/profile.html', context)


def confidential(request):
    pdf = open('memories/templates/confidential.pdf', 'rb')
    return FileResponse(pdf)


def delete(request):
    pdf = open('memories/templates/delete.pdf', 'rb')
    return FileResponse(pdf)
