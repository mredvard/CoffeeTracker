from django.conf.urls import url
from django.contrib.auth.views import (
    login,
    logout
)

from .views import (
    UserCreationView,
    LoginView,
    UserProfileView,
)

urlpatterns = [
    url(
        regex=r'^login/$',
        view=LoginView.as_view(),
        name='login',
    ),
    url(
        regex=r'^logout/$',
        view=logout,
        name='logout',
        kwargs={'next_page': 'home'}
    ),
    url(
        regex=r'^register/$',
        view=UserCreationView.as_view(),
        name='register',
        kwargs={'next_page': 'home'}
    ),
    url(
        regex=r'^profile/$',
        view=UserProfileView.as_view(),
        name='profile',
    ),
]
