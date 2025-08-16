from django.urls import path
from .views import register, login
app_name = 'accounts'

urlpatterns = [
    path('', register, name='register'),  # Now /accounts/ shows the register page
    path('login/', login, name='login'),

]