from django.conf.urls import url, include

from .views import index
from .views import hardware

urlpatterns = [
    # url(r'', views.index),
    url(r'0bfc4ef8ad064c1d3ac1af7ba3f4efc986906e41b330f23424/', index.as_view()),
    url(r'hardware/', hardware.as_view())
]
