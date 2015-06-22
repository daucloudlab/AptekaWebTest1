from django.conf.urls import url
from apteka.views import all_apteks, add_apteks, add_apteks_process
urlpatterns = [
    url(r'^$', all_apteks),
    url(r'^add/$', add_apteks),
    url(r'^add_process/$', add_apteks_process),
]
