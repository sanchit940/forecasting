from django.urls import include, path, re_path
from django.contrib import admin
from swag.views import *
from users.views import *


urlpatterns = [
    # Examples:
    path('', home_page, name='home_page'),
    path('form/', FormView, name='form_page'),
    path('login/', LoginView, name='login_page'),
    path('register/', RegistrationView, name='register_page'),
    path('logout/', LogoutView, name='logout_page'),
    path('show_data/', graph_plot, name='show_data'),
    path('admin/', admin.site.urls),
    path('show_forecasted_smavg_data/', forecasted_plot, name='forecasted_plot')
]