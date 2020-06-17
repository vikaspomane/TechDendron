from django.urls import path, include
from common_account.views import common_views


urlpatterns = [

    path('home',common_views.home_page)
]
