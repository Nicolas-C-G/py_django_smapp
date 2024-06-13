from django.shortcuts import render
from .forms import PostCreateForm
# Create your views here.

def post_create(request):
    if request.method == 'POST':
        form = PostCreateForm(data=request.POST)
        if form.is_valid():
            form.save()