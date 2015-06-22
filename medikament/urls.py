from django.conf.urls import url
from medikament.views import all_medikaments, add_medikaments, add_medikaments_process

urlpatterns = [
    url(r'^$', all_medikaments),
    url(r'^add/$', add_medikaments),
    url(r'^add_process/$', add_medikaments_process),
]
