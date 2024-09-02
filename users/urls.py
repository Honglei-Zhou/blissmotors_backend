from django.urls import include, path, re_path
# from rest_framework.authtoken.views import obtain_auth_token
from . import views
from allauth.account.views import confirm_email

urlpatterns = [
    path('', include('rest_auth.urls')),
    path('socialaccount/facebook', views.FacebookLogin.as_view(), name='facebook_login'),
    path('accounts', views.UserList.as_view(), name='user-list'),
    path('account/', include('allauth.urls')),
    re_path(r'^registration/account-confirm-email/(?P<key>[-:\w]+)/$', confirm_email, name="account_confirm_email"),
    path('registration/', include('rest_auth.registration.urls')),
    path('registrationcodes', views.RegistrationCodeCreateView.as_view(), name='registration_code-createview'),
    path('registrationcodes/<int:pk>', views.RegistrationCodeView.as_view(), name='registration_code-view')
]
