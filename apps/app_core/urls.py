"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from .views import (
    FolderListView, CollectionListView, SharedUserListView,
    ProfileDetailView, FolderDetailView, CollectionDetailView,
    ProfileCreateView, FolderCreateView, CollectionCreateView,
    ProfileUpdateView, FolderUpdateView, CollectionUpdateView,
    ProfileDeleteView, FolderDeleteView, CollectionDeleteView,
    TagCreateView, TagUpdateView, TagDeleteView,
    create_collection, SharedFolderCreateView, SharedFolderListView,
    CollectionAllListView, CollectionDeletedListView, CollectionArchivedListView,
    TagListView, getSharedCode, CollectionArchiveView, getSharedTag, getShareLink,
    CollectionRecoverView, CollectionRealDeleteView, CollectionSearchView
)

urlpatterns = [
    # path('profiles/', ProfileListView.as_view(), name='profile-list'),
    path('profile/create/', ProfileCreateView.as_view(), name='profile-create'),
    path('profile/<int:pk>/', ProfileDetailView.as_view(), name='profile-detail'),
    path('profile/<int:pk>/update/', ProfileUpdateView.as_view(), name='profile-update'),
    path('profile/<int:pk>/delete/', ProfileDeleteView.as_view(), name='profile-delete'),
    path('profile/<int:profile_pk>/create_collection/', create_collection, name='create_collection'),

    path('profile/<int:profile_pk>/folders/', FolderListView.as_view(), name='folder-list'),
    path('profile/<int:profile_pk>/sharefolders/', SharedFolderListView.as_view(), name='sharefolder-list'),
    path('profile/<int:profile_pk>/all/', CollectionAllListView.as_view(), name='all-collection-list'),
    path('profile/<int:profile_pk>/del/', CollectionDeletedListView.as_view(), name='del-collection-list'),
    path('profile/<int:profile_pk>/archive/', CollectionArchivedListView.as_view(), name='archive-collection-list'),
    path('profile/<int:profile_pk>/sharedfolder/<int:folder_pk>/users/', SharedUserListView.as_view(), name='shared-user-list'),
    path('profile/<int:profile_pk>/tags/', TagListView.as_view(), name='tag-list'),
    path('profile/<int:profile_pk>/folders/<int:folder_pk>/sharedcode/', getSharedCode, name='shared-code-list'),
    path('sharedtag/', getSharedTag, name='shared-tag-list'),
    path('profile/<int:profile_pk>/folder/<int:folder_pk>/collection/<int:pk>/link', getShareLink, name='shared-link'),

    path('profile/<int:profile_pk>/folder/create/', FolderCreateView.as_view(), name='folder-create'),
    path('profile/<int:profile_pk>/folder/<int:pk>/', FolderDetailView.as_view(), name='folder-detail'),
    path('profile/<int:profile_pk>/folder/<int:pk>/update/', FolderUpdateView.as_view(), name='folder-update'),
    path('profile/<int:profile_pk>/folder/<int:pk>/delete/', FolderDeleteView.as_view(), name='folder-delete'),
    path('profile/<int:profile_pk>/sharedfolder/create/', SharedFolderCreateView.as_view(), name='shared-folder-create'),

    path('profile/<int:profile_pk>/folder/<int:folder_pk>/collections/', CollectionListView.as_view(),
         name='collection-list'),
    path('profile/<int:profile_pk>/folder/<int:folder_pk>/collection/create/', CollectionCreateView.as_view(),
         name='collection-create'),
    path('profile/<int:profile_pk>/folder/<int:folder_pk>/collection/<int:pk>/', CollectionUpdateView.as_view(),
         name='collection-detail'),
    path('profile/<int:profile_pk>/collection/<int:pk>/', CollectionUpdateView.as_view(),
         name='collection-detail'),
    path('profile/<int:profile_pk>/folder/<int:folder_pk>/collection/<int:pk>/archive/', CollectionArchiveView.as_view(),
          name='collection-update'),
    path('profile/<int:profile_pk>/folder/<int:folder_pk>/collection/<int:pk>/delete/', CollectionDeleteView.as_view(),
        name='collection-delete'),
    path('profile/<int:profile_pk>/folder/<int:folder_pk>/collection/<int:pk>/recover/', CollectionRecoverView.as_view(),
        name='collection-recover'),
    path('profile/<int:profile_pk>/folder/<int:folder_pk>/collection/<int:pk>/realdel/', CollectionRealDeleteView.as_view(),
        name='collection-recover'),

    path('profile/<int:pk>/search', CollectionSearchView.as_view(), name='search-collection'),
    path('profile/<int:profile_pk>/collection/create/', CollectionCreateView.as_view(),name='collection-create-nofolder'),
    path('profile/<int:profile_pk>/tag/create/', TagCreateView.as_view(), name='tag-create'),
    path('profile/<int:profile_pk>/tag/<int:pk>/edit', TagUpdateView.as_view(), name='tag-update'),
    path('profile/<int:profile_pk>/tag/<int:pk>/delete', TagDeleteView.as_view(), name='tag-delete'),
]
