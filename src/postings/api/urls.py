from django.conf.urls import url
from .views import KhassidaPostRudView, KhassidaPostAPIView

app_name = 'postings'

urlpatterns = [
    url(r'^$', KhassidaPostAPIView.as_view(), name='post-listcreate'),
    url(r'^(?P<pk>\d+)/$', KhassidaPostRudView.as_view(), name='post-rud')
]
