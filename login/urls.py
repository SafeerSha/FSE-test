from django.urls import path
from.import views

urlpatterns = [
    path('',views.home),
    path('login',views.log),
    path("signup",views.signup),
    path(r'^login/submit/$',views.dashbord),
    path('loginn',views.signin),
    path('submit1',views.registration),
    path('submit',views.signin),
    path('/go',views.approved),
]
