from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<questionid>[0-9]+)/$', views.chatIndex.as_view(), name='chat_index'),
    url(r'^response/$', views.chat_index, name='chat_response'),
]
