"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app.views import post, composer, production

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'$', post.show_list),
    url(r'^post/list/(?P<page>\d+)/$',view=post.show_list),
    url(r'^user/oneuser/userid-(?P<cid>\d+)/$', view=composer.oneuser),
    url(r'^a(?P<pid>\d+)/$', view=production.articleList)
#http://127.0.0.1:8000/a10176335?from=ArticleList
]
