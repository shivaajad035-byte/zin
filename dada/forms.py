from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import UserProfile, Education, SocialMedia

User = get_user_model()

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'
        exclude = ['user']

class SocialMediaForm(forms.ModelForm):
    class Meta:
        model = SocialMedia
        fields = '__all__'
        exclude = ['user_profile']

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = '__all__'
        exclude = ['user_profile']
