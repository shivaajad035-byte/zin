from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import Home, CustomLoginView, SignupView, edit_profile, CustomLogoutView

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('userdata/', edit_profile, name='userdata'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
