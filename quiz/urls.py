from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^$', views.draw_number_view, name='draw_number'),
]