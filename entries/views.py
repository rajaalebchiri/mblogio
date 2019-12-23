from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from .models import Entry, Category, Profile
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.models import User

class Posts(ListView):
    model = Entry
    context_object_name = "posts"
    template_name='entries/posts.html'


def HomeView(request):
    entries = Entry.objects.all()
    categories = Category.objects.all()
    context = {
        'blog_entries': entries,
        'categories': categories
    }
    return render(request, 'entries/index.html', context)

def CategorySingleView(request, pk):

    # Filter posts by tag name
    posts = Entry.objects.filter(entry_category_id=pk)
    pkk = Category.objects.filter(id=pk)
    context = {
        'pkk':pkk,
        'posts':posts
    }
    return render(request, 'entries/category_single.html', context)

class CategoryView(ListView):
    model = Category
    context_object_name = "blog_entries"
    template_name = 'entries/categories.html'

class EntryView(DetailView):
    model = Entry
    template_name = "entries/blog-single.html"

class CreateEntryView(CreateView):
    model = Entry
    template_name = 'entries/create_entry.html'
    fields = {'entry_title', 'entry_text', 'entry_category', 'picture'}

    def form_valid(self, form):
        form.instance.entry_author = self.request.user
        form.instance.picture = form.cleaned_data.get('picture')
        return super().form_valid(form)

class AddCategory(CreateView):
    model = Category
    template_name = 'entries/add_category.html'
    fields = {'name', 'slug'}

class UserPostListView(ListView):
    model = Entry
    template_name = 'entries/user_posts.html' 
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Entry.objects.filter(entry_author=user).order_by('-entry_date')

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.Profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            
            return redirect('profile')

    else:
        users_without_profile = User.objects.filter(Profile__isnull=True)
        for user in users_without_profile:
            c = Profile.objects.create(User=request.user)
            c.save()
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.Profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'entries/profile.html', context)
