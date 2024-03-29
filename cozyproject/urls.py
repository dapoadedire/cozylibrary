"""cozyproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path

from accounts.forms import EmailValidationOnForgotPassword

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("cozylibrary.urls")),
    path(
        "accounts/password_reset/",
        auth_views.PasswordResetView.as_view(
            form_class=EmailValidationOnForgotPassword
        ),
        name="password_reset",
    ),
    path("accounts/", include("accounts.urls")),
    path("accounts/", include("django.contrib.auth.urls")),  # for login/logout
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
handler404 = "cozylibrary.views.custom_page_not_found_view"
handler500 = "cozylibrary.views.custom_error_view"
handler403 = "cozylibrary.views.custom_permission_denied_view"
handler400 = "cozylibrary.views.custom_bad_request_view"

# The URLs provided by auth are:

# accounts/login/ [name='login']
# accounts/logout/ [name='logout']
# accounts/password_change/ [name='password_change']
# accounts/password_change/done/ [name='password_change_done']
# accounts/password_reset/ [name='password_reset']
# accounts/password_reset/done/ [name='password_reset_done']
# accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
# accounts/reset/done/ [name='password_reset_complete']
