from django.contrib.auth.views import LoginView as DefaultLoginView
from django.shortcuts import reverse


class LoginView(DefaultLoginView):
    template_name = 'main/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        url = super().get_redirect_url()
        if hasattr(self.request.user, 'companyprofile'):
            return url or reverse('company:job-offers-added')
        elif hasattr(self.request.user, 'studentprofile'):
            return url or reverse('student:detail')
        else:
            return url
