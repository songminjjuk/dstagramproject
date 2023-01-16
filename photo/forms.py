from django import forms

from .models import Profile, Comment


class ProfileForm(forms.ModelForm):
    profile_photo = forms.ImageField(required=False) # 선택적으로 입력할 수 있음.
    class Meta:
        model = Profile
        fields = ['profile_photo']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
