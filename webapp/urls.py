from django.conf.urls import url

from .views import dashboard

urlpatterns = [
    url(
        regex=r'^dashboard/$',
        view=dashboard,
        name='dashboard'
    ),
]
