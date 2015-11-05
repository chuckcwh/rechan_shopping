from django.conf.urls import patterns, url

urlpatterns = patterns (
    '',
    url(r'^$', HomeView.as_view(), name='index'),
)