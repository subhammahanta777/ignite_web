from django.conf.urls import include, url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    #test/question_id
    url(r'^(?P<questionid>[0-9]+)/$', views.details, name='details'),
    #test/question_id/check/
    url(r'^(?P<questionid>[0-9]+)/check/$', views.check, name='check'),
    #test/question_id/check/??csrfmiddlewaretoken
    # url(r'^(?P<questionid>[0-9]+)/check/?csrfmiddlewaretoken', views.details, name='check')
    url(r'^done/$', views.analysis, name='analysis'),
    url(r'^out_of_question/$', views.analysis, name='out_of_question')
]
