"""MyBook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from website import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^login/$', views.login),
	url(r'^signup/$', views.signup),
	url(r'^logout/$', views.logout),
	url(r'^add/img$', views.add_image),
	url(r'^add/vid$', views.add_video),
	url(r'^add/msg$', views.add_message),
	url(r'^uploads/(?P<username>[-_\w\d]+)/(?P<filename>[-_\w\d]+)/$', views.get_uploaded_file),
	url(r'^user/(?P<username>[-_\w\d]+)/$', views.user_profile),
	url(r'^follow/(?P<username>[-_\w\d]+)/$', views.follow_user),
	url(r'^unfollow/(?P<username>[-_\w\d]+)/$', views.unfollow_user),
    url(r'^admin/', admin.site.urls),
]
