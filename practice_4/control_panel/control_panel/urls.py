from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    '',
    url(r'^$', 'library.views.index'),
    url(r'^library/$', 'library.views.index'),
    url(r'^library/books/$', 'library.views.index'),
    url(r'^library/books/(\d+)/$', 'library.views.bookCard'),
    url(r'^library/authors/$', 'library.views.authors'),
    url(r'^library/authors/(\d+)/$', 'library.views.authorsCard'),
)
