from django.urls import path, include
from .views import HomeView, EntryView, CreateEntryView, CategoryView, Posts, CategorySingleView, AddCategory,  profile, UserPostListView
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.HomeView, name='blog-home'),
    path('posts', Posts.as_view(), name='posts'),
    path('entry/<int:pk>/', EntryView.as_view(), name='entry-detail'),
    path('create_entry', CreateEntryView.as_view(success_url='/'), name = "create_entry"),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('profile', views.profile, name='profile'),
    path('create_category', AddCategory.as_view(success_url='/'), name = "create_category"),
    path('categories', CategoryView.as_view(), name='categoryView'),
    path('category/<int:pk>/', views.CategorySingleView, name='category-detail')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)