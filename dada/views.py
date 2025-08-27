from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, FormView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LogoutView
from django.contrib.auth import get_user_model
from .forms import SignUpForm, UserProfileForm, SocialMediaForm, EducationForm
from .models import UserProfile, SocialMedia, Education

User = get_user_model()

class Home(ListView):
    model = User
    template_name = 'index.html'
    context_object_name = 'users'

class CustomLoginView(FormView):
    template_name = 'user_page/login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('home')

@login_required
def edit_profile(request):
    user = request.user
    user_profile, _ = UserProfile.objects.get_or_create(user=user)
    social_media, _ = SocialMedia.objects.get_or_create(user_profile=user_profile)
    education, _ = Education.objects.get_or_create(user_profile=user_profile)

    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        social_form = SocialMediaForm(request.POST, instance=social_media)
        education_form = EducationForm(request.POST, instance=education)

        if profile_form.is_valid() and social_form.is_valid() and education_form.is_valid():
            profile_form.save()
            social_form.save()
            education_form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect('userdata')
        else:
            messages.error(request, "Please correct the errors below.")

    else:
        profile_form = UserProfileForm(instance=user_profile)
        social_form = SocialMediaForm(instance=social_media)
        education_form = EducationForm(instance=education)

    return render(request, 'userdata.html', {
        'profile_form': profile_form,
        'social_form': social_form,
        'education_form': education_form
    })

class SignupView(FormView):
    template_name = 'user_page/signup.html'
    form_class = SignUpForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        messages.success(self.request, "Account created successfully!")
        return redirect(self.success_url)

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')

