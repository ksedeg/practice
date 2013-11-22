from django.conf.urls import patterns, include, url
from django.contrib import admin

from control_panel import settings
#from control_panel.settings import MEDIA_ROOT
from orders.models import *
from search.models import *
from django.conf.urls import patterns, url
from library.views import *

from django.contrib.auth.views import login, logout
from django.contrib.auth.forms import AuthenticationForm
from library.views import register

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^login/$', login),
    url(r'^logout/$', logout),
    url(r'^register/$', register),
    url(r'^library/$', BookListView.as_view()),
    url(r'^library/books/$', BookListView.as_view()),
    url(r'^library/books/(?P<pk>\d+)/$', BookCardView.as_view(), name='book_id'),
    url(r'^library/authors/$', AuthorsListView.as_view()),
    url(r'^library/authors/(?P<pk>\d+)/$', AuthorCardView.as_view(), name='author_id'),
    url(r'^upload/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT, }),
    url(r'^orders.html', CustomersList.as_view()),
    url(r'^customer.html/(?P<slug>[-_\w]+)/$', CustomerDetails.as_view()),
    url(r'^book_search.html', 'search.views.search'),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^$', 'library.views.index'),
    #url(r'^library/$', 'library.views.index'),
    #url(r'^library/books/$', 'library.views.index'),
    #url(r'^library/books/(\d+)/$', 'library.views.bookCard'),
    #url(r'^library/authors/$', 'library.views.authors'),
    #url(r'^library/authors/(\d+)/$', 'library.views.authorsCard'),
    #url(r'^images/(?P<path>.*)$', 'django.views.static.serve', {
    #    'document_root': settings.MEDIA_ROOT, }),

)
