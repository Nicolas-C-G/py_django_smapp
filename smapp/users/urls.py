from django.urls import path, reverse_lazy
from . import views
from django.contrib.auth import views as auth_view


app_name = 'users'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('password_change/',auth_view.PasswordChangeView.as_view(template_name='users/password_change_form.html', success_url='done'), name='password_change'),
    path('password_change/done/', auth_view.PasswordChangeDoneView.as_view(template_name='users/password_change_done.html'), name='done'),
    path('password_reset/', auth_view.PasswordResetView.as_view(template_name='users/password_reset_form.html', success_url='prdone'), name='password_reset'),
    path('password_reset/done/', auth_view.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='prdone'),
    path('reset/<int:uidb64>/<str:token>', auth_view.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html', success_url='prcomplete'), name='password_reset_confirm'),
    path('reset/done/', auth_view.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='prcomplete'),
]