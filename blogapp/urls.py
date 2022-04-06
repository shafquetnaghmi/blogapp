from django.urls import path 
from . import views 
from .views import signupview
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
app_name='blogapp'
urlpatterns=[
    path('',views.home,name='home'),
    path('createblog/',views.blogview,name='blogview'),
    path('blog/',views.blogretrieve,name='blog'),
    path('signup/',views.signupview,name='signup'),
    path('login/',views.loginview,name='login'),
    path('logout/',views.logoutview,name='logout'),
    path('author/<int:pk>/',views.authorview,name='author'),
    path('blogdata/<str:pk>/',views.blog,name='blogdata'),
    path('profile/<str:pk>/',views.profile,name='profile'),
    path('change-password/', auth_views.PasswordChangeView.as_view(template_name='blogapp/change-password.html',success_url=reverse_lazy('blogapp:password_change_done')),name='change-password'),
    path('password_change/done/',auth_views.PasswordChangeDoneView.as_view(template_name='blogapp/password_change_done.html'),name='password_change_done'),
   
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name='blogapp/reset_password.html',
            success_url=reverse_lazy('blogapp:password_reset_done'),
            email_template_name='blogapp/reset_password_email.html'
            ),name='reset_password'),  
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name='blogapp/reset_password_sent.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='blogapp/reset_password_cofirm.html',
            success_url = reverse_lazy("blogapp:password_reset_complete")),name='password_reset_confirm'),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='blogapp/password_reset_complete.html'),name='password_reset_complete'),
    
]