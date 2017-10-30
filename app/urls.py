from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'get/(?P<schedule_id>[^/]+)', views.get, name='get'),
    url(r'index/', views.index, name='index'),
]
