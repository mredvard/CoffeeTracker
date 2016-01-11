import logging

from braces.views import LoginRequiredMixin

from django.contrib.auth import login, authenticate, REDIRECT_FIELD_NAME
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ImproperlyConfigured
from django.shortcuts import resolve_url, redirect
from django.utils.http import is_safe_url
from django.views.generic import FormView

from .forms import UserCreationForm, ProfileForm

logger = logging.getLogger(__name__)


class CTUserView(FormView):
    success_url = 'home'

    def get_success_url(self):
        """
        Returns the supplied success URL.
        """
        if not self.success_url:
            raise ImproperlyConfigured(
                "No URL to redirect to. Provide a success_url.")
        redirect_to = self.request.POST.get(
            REDIRECT_FIELD_NAME,
            self.request.GET.get(REDIRECT_FIELD_NAME, self.success_url)
        )
        # Ensure the user-originating redirection url is safe.
        if not is_safe_url(url=redirect_to, host=self.request.get_host()):
            logger.debug('URL not safe: %s' % redirect_to)
            redirect_to = resolve_url(self.success_url)

        return redirect_to


class UserCreationView(CTUserView):
    form_class = UserCreationForm
    template_name = 'users/register.html'

    def form_valid(self, form):
        form.save()
        user = authenticate(
            username=form.cleaned_data['email'],
            password=form.cleaned_data['password1']
        )
        login(self.request, user)
        return redirect(self.get_success_url())


class LoginView(CTUserView):
    template_name = 'users/login.html'
    form_class = AuthenticationForm

    def form_valid(self, form):
        user = authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password']
        )
        login(self.request, user)
        return redirect(self.get_success_url())


class UserProfileView(LoginRequiredMixin, CTUserView):
    template_name = 'users/profile.html'
    form_class = ProfileForm

    def get(self, request, *args, **kwargs):
        form = ProfileForm(instance=self.request.user)
        return self.render_to_response(self.get_context_data(form=form))

    def post(self, request, *args, **kwargs):
        form = ProfileForm(data=request.POST, instance=self.request.user)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        form.save()
        return redirect(self.get_success_url())
