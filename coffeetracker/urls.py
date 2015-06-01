from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', TemplateView.as_view(
        template_name="website/home.html"), name='home'),

    url(r'^webapp/$',
        include('webapp.urls', namespace='webapp', app_name='webapp')),
    url(r'^admin/', include(admin.site.urls)),
]
