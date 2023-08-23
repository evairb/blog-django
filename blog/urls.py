from django.urls import path
from blog import views
from blog.views import (PostListView, CreatedByListView, CategoryListView, TagListViews,
                        SearchListView,PageDetailView,PostDeteilView)
    

app_name = 'blog'

urlpatterns = [
    path('', PostListView.as_view(), name='index'),
    path('page/<slug:slug>/', PageDetailView.as_view(), name='page'),
    path('post/<slug:slug>/', PostDeteilView.as_view(), name='post'),
    path('created_by/<int:author_pk>/', CreatedByListView.as_view(), name='created_by'),
    path('category/<slug:slug>/', CategoryListView.as_view(), name='category'),
    path('tag/<slug:slug>/', TagListViews.as_view(), name='tag'),
    path('search/', SearchListView.as_view(), name='search')
]
