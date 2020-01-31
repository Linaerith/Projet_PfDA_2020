from django.conf.urls import url
from prediction import views
urlpatterns = [
    url(r'^predict/$' , views.predict),
    url(r'^events/$' , views.event_list ),
    url(r'^event/(?P<pk>[0-9]+)/$' ,views.event_detail),
]
