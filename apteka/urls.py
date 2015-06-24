from django.conf.urls import url
from apteka.views import all_apteks, add_apteks, del_apteks, update_apteks
urlpatterns = [
    url(r'^$', all_apteks),
    url(r'^add/$', add_apteks),
    url(r'^del/$', del_apteks),
    url(r'^update/(?P<id>\w+)/$',update_apteks),

]
