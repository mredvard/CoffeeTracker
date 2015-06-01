from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^dashboard/$',
        view=views.dashboard,
        name='dashboard'
    ),
]
