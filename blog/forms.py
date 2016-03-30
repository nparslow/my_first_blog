
from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post # use the Post model
        fields = ('title', 'text',)
        # don't want author as it will be the person logged in