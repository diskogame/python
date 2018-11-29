from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detailURL'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='resultsURL'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='voteURL'),

    url('all', views.all_questions, name='all_questions'),
    url('create', views.create, name='create'),
    url(r'^update/(?P<question_id>[0-9]+)$', views.update, name='update'),
    url(r'^delete/(?P<question_id>[0-9]+)$', views.delete, name='delete'),

    url('nuevoObjeto', views.nuevoObjeto, name='nuevoObjeto'),

]
