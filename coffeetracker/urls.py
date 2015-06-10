from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [

    # Local apps
    url(r'^$', TemplateView.as_view(
        template_name="website/home.html"), name='home'),
    url(r'^webapp/$',
        include('webapp.urls', namespace='webapp', app_name='webapp')),
    url(r'^coffeemaker/$',
        include('coffeemaker.urls', namespace='coffeemaker', app_name='coffeemaker')),

    # Django's Admin
    url(r'^ct_admin/', include(admin.site.urls)),

    # REST Framework
    url(r'^api-auth/',
        include('rest_framework.urls', namespace='rest_framework'))
]
