from django.conf.urls import url
from apteka.views import all_apteks, add_apteks
urlpatterns = [
    url(r'^$', all_apteks),
    url(r'^add/$', add_apteks),

]
