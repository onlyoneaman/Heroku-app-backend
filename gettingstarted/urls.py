from django.urls import path, include

from django.contrib import admin
from django.conf.urls import url

admin.autodiscover()

import hello.views
import customer.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", hello.views.index, name="index"),
    path("db/", hello.views.db, name="db"),
    path("admin/", admin.site.urls),
    url(r'^api/connect', customer.views.start_connection),
    url(r'^api/customers/$', customer.views.customers_list),
    url(r'^api/customers/(?P<pk>[0-9]+)$', customer.views.customers_detail),
]
