from dataclasses import field
from email import message
from pyexpat import model
from django import forms
from .models import *


class NewTopicForm(forms.ModelForm):
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={"rows": 5, "placeholder": "What is on your mind?"}
        ),
        max_length=40000,
        help_text="The max length of the text is 4000",
    )

    class Meta:
        model = Topic
        fields = ["subject", "message"]
