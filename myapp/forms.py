# if we are making a database driven app we need to make forms
from django import forms

from models import UserModel, PostModel, LikeModel, CommentModel

# Forms are created in order to picturize a way in which web pages will be displayed.


class SignUpForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['username', 'name', 'email', 'password']


class LoginForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['username', 'password']


class PostForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = ['image', 'caption']


class LikeForm(forms.ModelForm):
    class Meta:
        model = LikeModel
        fields = ['post']


class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = ['comment_text', 'post']
