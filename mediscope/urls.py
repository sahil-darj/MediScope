from django.contrib import admin
from django.urls import path, include
from predictor import views as predictor_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', predictor_views.home, name='home'),  # Home page
    path('predict/', include('predictor.urls')),   # Predictor URLs
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('', include('predictor.urls')),  # ✅ This includes signup & home
    path('accounts/', include('django.contrib.auth.urls')),  # ✅ For login/logout
   
]