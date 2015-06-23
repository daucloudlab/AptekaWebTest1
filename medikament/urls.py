from django.conf.urls import url
from medikament.views import all_medikaments, add_medikaments, del_medikaments

urlpatterns = [
    url(r'^$', all_medikaments),
    url(r'^add/$', add_medikaments),
    url(r'^del/$', del_medikaments),

]
