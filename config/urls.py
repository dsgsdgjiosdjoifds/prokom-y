from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin', admin.site.urls),

    path('api/auth', include('accounts.auth_urls')),
    path('api/accounts', include('accounts.urls')),
    path('api/posts', include('posts.urls')),
]
